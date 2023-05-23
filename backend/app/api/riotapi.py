from ..models import User, now, Match, Version, Champion, MatchDetail
from .collecter import Collecter
from ..extensions import db
from .ddragon import add_version, isinDB_version

collecter = Collecter()

def isinAPI_user(name):
    user = collecter.get_playerDto('name', name)
    if len(user.keys())==7:
        return True
    else:
        return False

def isinDB_user(puuid):
    user = User.query.filter(User.puuid==puuid).first()
    if user!=None:
        return True
    else:
        return False

def add_user(puuid):

    userDto = collecter.get_playerDto('puuid', puuid)
    user = User(puuid, userDto['name'], userDto['summonerLevel'], userDto['profileIconId'])
    db.session.add(user)
    db.session.commit()
    db.session.close()

def update_user_info(puuid):
    userDto = collecter.get_playerDto('puuid', puuid)
    User.query.filter(User.puuid==puuid).update({'name':userDto['name'], 'level':userDto['summonerLevel'], 'icon_id':userDto['profileIconId'], 'update_at':now})

    db.session.commit()
    db.session.close()
    print('update_user')

def test_update(puuid):
    matchHistory = []
    start = 0
    count = 20
    
    matchHistory.extend(collecter.get_matchHistory(puuid, start, count))
    needToUpdateMatchCount = len(matchHistory) - len(MatchDetail.query.filter(MatchDetail.puuid==puuid).all())

    if needToUpdateMatchCount==0:
        print('do not need to update[MatchHistory]')
    else:
        for i, m in enumerate(matchHistory[:needToUpdateMatchCount]):
            add_match(m)
            print(f'add match {i}/total {needToUpdateMatchCount}')

def update_user_matchHistory(puuid):

    matchHistory = []
    start = 0
    count = 100

    while True:
        matchHistory.extend(collecter.get_matchHistory(puuid, start, count))
        
        if len(matchHistory)%100!=0:
            break
        else:
            start = start + 100
    
    needToUpdateMatchCount = len(matchHistory) - len(MatchDetail.query.filter(MatchDetail.puuid==puuid).all())

    if needToUpdateMatchCount==0:
        print('do not need to update[MatchHistory]')
    else:
        for i, m in enumerate(matchHistory[:needToUpdateMatchCount]):
            add_match(m)
            print(f'add match {i}/total {needToUpdateMatchCount}')
    
def add_match(matchId):
    dto = collecter.get_matchDto(matchId)

    season = dto['info']['gameVersion'].split('.')[0]
    num1 = dto['info']['gameVersion'].split('.')[1]
    
    if isinDB_version(season, num1)==False:
        print('False')
        add_version(season, num1)
    
    # add_match[Match]

    version_id = Version.query.filter(Version.season==season, Version.num1==num1).with_entities(Version.id).first().id
    winTeam = (0 if dto['info']['teams'][0]['win']==True else 1)
    newMatch = Match(matchId, dto['info']['gameVersion'], version_id, winTeam)
    db.session.add(newMatch)
    db.session.commit()

    # add_match[MatchDetail]

    for p in dto['info']['participants']:
        key = p['championId']
        id = matchId + '0' * (4-len(str(key))) + str(key)
        puuid = p['puuid']
        # add_user
        if isinDB_user(puuid)==False:
            add_user(puuid)
        champion_id = Champion.query.filter(Champion.version_id==version_id, Champion.key==key).with_entities(Champion.id).first().id

        matchDetail = MatchDetail(id, matchId, champion_id, puuid)
        db.session.add(matchDetail)
        db.session.commit()

    db.session.close()
