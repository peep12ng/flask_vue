from ..models import Summoner, now, Match, Version, Champion, MatchDetail, Item, Perk, PerkStyle
from .collecter import Collecter
from ..extensions import db
from .ddragon import add_version, isinDB_version

collecter = Collecter()

def get_isinAPI_summoner(name):
    status = collecter.get_summonerStatus(name)
    if status==200:
        return True
    else:
        return False

def get_isinDB_summoner(puuid):
    summoner = Summoner.query.filter(Summoner.puuid==puuid).first()
    if summoner!=None:
        return True
    else:
        return False

def add_summoner(puuid):

    summonerDto = collecter.get_summonerDto('puuid', puuid)
    summoner = Summoner(puuid, summonerDto['name'], summonerDto['summonerLevel'], summonerDto['profileIconId'])
    db.session.add(summoner)
    db.session.commit()
    db.session.close()

def update_summoner_info(puuid):
    summonerDto = collecter.get_summonerDto('puuid', puuid)
    Summoner.query.filter(Summoner.puuid==puuid).update({'name':summonerDto['name'], 'level':summonerDto['summonerLevel'], 'icon_id':summonerDto['profileIconId'], 'update_at':now})

    db.session.commit()
    db.session.close()
    print('update_summoner_info')

def test_update(puuid):
    matches = []
    start = 0
    count = 5
    
    matches = collecter.get_matchHistory(puuid, start, count)
    inDBMatches = [md.match_id for md in MatchDetail.query.filter(MatchDetail.puuid==puuid).all()]

    matchesWhatNeedToAdd = list(set(matches) - set(inDBMatches))

    if len(matchesWhatNeedToAdd)==0:
        print("do not need to add match")
    else:            
        for i, m in enumerate(matchesWhatNeedToAdd):
            add_match(m)
            print(f'add match {i+1}/total {len(matchesWhatNeedToAdd)}')

def update_summoner_matchHistory(puuid):

    allMatches = []
    start = 0
    count = 100

    while True:
        allMatches.extend(collecter.get_matchHistory(puuid, start, count))
        
        if len(allMatches)%100!=0:
            break
        else:
            start = start + 100

    inDBMatches = [md.match_id for md in MatchDetail.query.filter(MatchDetail.puuid==puuid).all()]

    matchesWhatNeedToAdd = list(set(allMatches) - set(inDBMatches))

    if len(matchesWhatNeedToAdd)==0:
        print("do not need to add match")
    else:            
        for i, m in enumerate(matchesWhatNeedToAdd):
            add_match(m)
            print(f'add match {i+1}/total {len(matchesWhatNeedToAdd)}')
    
def add_match(matchId):
    dto = collecter.get_matchDto(matchId)

    season = int(dto['info']['gameVersion'].split('.')[0])
    num1 = int(dto['info']['gameVersion'].split('.')[1])
    
    if isinDB_version(season, num1)==False:
        print(season, num1)
        print('False')
        add_version(season, num1, 1)
    
    # add_match[Match]

    version_id = Version.query.filter(Version.season==season, Version.num1==num1).with_entities(Version.id).first().id
    winTeam = (100 if dto['info']['teams'][0]['win']==True else 200)
    firstBloodTeam = (100 if dto['info']['teams'][0]['objectives']['champion']['first']==True else 200)
    firstTowerTeam = (100 if dto['info']['teams'][0]['objectives']['tower']['first']==True else 200)
    firstInhibitorTeam = (100 if dto['info']['teams'][0]['objectives']['inhibitor']['first']==True else 200)
    isEarlySurrendered = (True if (dto['info']['participants'][0]['teamEarlySurrendered']==True)&(dto['info']['participants'][5]['teamEarlySurrendered']==True) else False)
    gameStartTimeStamp = dto['info']['gameStartTimestamp']
    gameDuration = dto['info']['gameDuration']
    newMatch = Match(matchId, dto['info']['gameVersion'], version_id, gameStartTimeStamp, gameDuration,
                    winTeam, firstBloodTeam, firstTowerTeam, firstInhibitorTeam, isEarlySurrendered)
    db.session.add(newMatch)
    db.session.commit()

    # add_match[MatchDetail]

    for p in dto['info']['participants']:
        participantId = p['participantId']
        id = matchId + '0' * (2-len(str(participantId))) + str(participantId)
        champion_key = p['championId']
        champion_id = 'C' + version_id + '0' * (4-len(str(champion_key))) + str(champion_key)
        puuid = p['puuid']
        # add_user
        if get_isinDB_summoner(puuid)==False:
            add_summoner(puuid)
        champlevel = p['champLevel']
        goldEarend = p['goldEarned']
        goldSpent = p['goldSpent']
        print(type(p['item0']))
        item0_id = 'I' + version_id + (str(p['item0']) if p['item0']!=0 else '0000')
        item1_id = 'I' + version_id + (str(p['item1']) if p['item1']!=0 else '0000')
        item2_id = 'I' + version_id + (str(p['item2']) if p['item2']!=0 else '0000')
        item3_id = 'I' + version_id + (str(p['item3']) if p['item3']!=0 else '0000')
        item4_id = 'I' + version_id + (str(p['item4']) if p['item4']!=0 else '0000')
        item5_id = 'I' + version_id + (str(p['item5']) if p['item5']!=0 else '0000')
        item6_id = 'I' + version_id + (str(p['item6']) if p['item6']!=0 else '0000')

        itemsPurchased = p['itemsPurchased']
        longestTimeSpentLiving = p['longestTimeSpentLiving']

        statPerks = p['perks']['statPerks']
        shardDefense_id = 'SH'+ str(statPerks['defense'])
        shardFlex_id = 'SH' + str(statPerks['flex'])
        shardOffense_id = 'SH' + str(statPerks['offense'])
        
        mainStyles = p['perks']['styles'][0]
        mainPerkStyle_id = 'PS' + version_id + str(mainStyles['style'])

        mainPerks = mainStyles['selections']
        mainPerk1_id = 'P' + version_id + str(mainPerks[0]['perk'])
        mainPerk2_id = 'P' + version_id + str(mainPerks[1]['perk'])
        mainPerk3_id = 'P' + version_id + str(mainPerks[2]['perk'])
        mainPerk4_id = 'P' + version_id + str(mainPerks[3]['perk'])

        subStyles = p['perks']['styles'][1]
        subPerkStyle_id = 'PS' + version_id + str(subStyles['style'])
        subPerks = subStyles['selections']
        subPerk1_id = 'P' + version_id + str(subPerks[0]['perk'])
        subPerk2_id = 'P' + version_id + str(subPerks[1]['perk'])

        matchDetail = MatchDetail(id, matchId, champion_id, puuid, participantId,
                                p['win'], p['kills'], p['deaths'], p['assists'],
                                champlevel, goldEarend, goldSpent,
                                item0_id, item1_id, item2_id, item3_id, item4_id, item5_id, item6_id,
                                itemsPurchased, longestTimeSpentLiving,
                                shardDefense_id, shardFlex_id, shardOffense_id,
                                mainPerkStyle_id,
                                mainPerk1_id, mainPerks[0]['var1'], mainPerks[0]['var2'], mainPerks[0]['var3'],
                                mainPerk2_id, mainPerks[1]['var1'], mainPerks[1]['var2'], mainPerks[1]['var3'],
                                mainPerk3_id, mainPerks[2]['var1'], mainPerks[2]['var2'], mainPerks[2]['var3'],
                                mainPerk4_id, mainPerks[3]['var1'], mainPerks[3]['var2'], mainPerks[3]['var3'],
                                subPerkStyle_id,
                                subPerk1_id, subPerks[0]['var1'], subPerks[0]['var2'], subPerks[0]['var3'],
                                subPerk2_id, subPerks[1]['var1'], subPerks[1]['var2'], subPerks[1]['var3']
                                )
        db.session.add(matchDetail)
        db.session.commit()

    db.session.close()