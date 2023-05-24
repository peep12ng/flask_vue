from ..models import Summoner, now, Match, Version, Champion, MatchDetail, Item
from .collecter import Collecter
from ..extensions import db
from .ddragon import add_version, isinDB_version

collecter = Collecter()

def isinAPI_summoner(name):
    status = collecter.get_summonerStatus(name)
    if status==200:
        return True
    else:
        return False

def isinDB_summoner(puuid):
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

    season = dto['info']['gameVersion'].split('.')[0]
    num1 = dto['info']['gameVersion'].split('.')[1]
    
    if isinDB_version(season, num1)==False:
        print('False')
        add_version(season, num1)
    
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
        championKey = p['championId']
        puuid = p['puuid']
        # add_user
        if isinDB_summoner(puuid)==False:
            add_summoner(puuid)
        champion_id = Champion.query.filter(Champion.version_id==version_id, Champion.key==championKey).first().id
        champlevel = p['champLevel']
        goldEarend = p['goldEarned']
        goldSpent = p['goldSpent']
        item0_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item0']).first().id if p['item0']!=0 else '0')
        item1_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item1']).first().id if p['item1']!=0 else '0')
        item2_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item2']).first().id if p['item2']!=0 else '0')
        item3_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item3']).first().id if p['item3']!=0 else '0')
        item4_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item4']).first().id if p['item4']!=0 else '0')
        item5_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item5']).first().id if p['item5']==0 else '0')
        item6_id = (Item.query.filter(Item.version_id==version_id, Item.key==p['item6']).first().id if p['item6']==0 else '0')
        itemsPurchased = p['itemsPurchased']
        longestTimeSpentLiving = p['longestTimeSpentLiving']

        matchDetail = MatchDetail(matchId, champion_id, puuid, participantId,
                                p['win'], p['kills'], p['deaths'], p['assists'],
                                champlevel, goldEarend, goldSpent,
                                item0_id, item1_id, item2_id, item3_id, item4_id, item5_id, item6_id,
                                itemsPurchased, longestTimeSpentLiving)
        db.session.add(matchDetail)
        db.session.commit()

    db.session.close()