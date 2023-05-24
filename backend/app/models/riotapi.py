from ..extensions import db
import datetime

now = datetime.datetime.now()

class Summoner(db.Model):
    puuid = db.Column(db.VARCHAR(100), primary_key=True)
    name = db.Column(db.VARCHAR(20))
    level = db.Column(db.Integer)
    icon_id = db.Column(db.VARCHAR(20))
    create_at = db.Column(db.DateTime, default=now)
    update_at = db.Column(db.DateTime, default=now)

    _matchDetail = db.relationship('MatchDetail', backref='summoner')

    def __init__(self, puuid, name, level, icon_id):
        self.puuid = puuid
        self.name = name
        self.level = level
        self.icon_id = icon_id

class Match(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    gameVersion = db.Column(db.VARCHAR(30))
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    gameStartTimeStamp = db.Column(db.BIGINT)
    gameDuration = db.Column(db.Integer)
    winTeam = db.Column(db.Integer)
    fisrtBloodTeam = db.Column(db.Integer)
    firstTowerTeam = db.Column(db.Integer)
    firstInhibitorTeam = db.Column(db.Integer)
    isEarlySurrendered = db.Column(db.Boolean)

    _matchDetail = db.relationship('MatchDetail', backref='match')

    def __init__(self, id, gameVersion, version_id, gameStartTimeStamp, gameDuration, 
                winTeam, fisrtBloodTeam, firstTowerTeam, firstInhibitorTeam, isEarlySurrendered):
        self.id = id
        self.gameVersion = gameVersion
        self.version_id = version_id
        self.gameStartTimeStamp = gameStartTimeStamp
        self.gameDuration = gameDuration
        self.winTeam = winTeam
        self.fisrtBloodTeam = fisrtBloodTeam
        self.firstTowerTeam = firstTowerTeam
        self.firstInhibitorTeam = firstInhibitorTeam
        self.isEarlySurrendered = isEarlySurrendered

class MatchDetail(db.Model):
    id = db.Column(db.VARCHAR(30), primary_key=True)
    match_id = db.Column(db.VARCHAR(20), db.ForeignKey('match.id'))
    champion_id = db.Column(db.VARCHAR(20), db.ForeignKey('champion.id'))
    puuid = db.Column(db.VARCHAR(100), db.ForeignKey('summoner.puuid'))
    participantId = db.Column(db.Integer)
    isWin = db.Column(db.Boolean)
    kills = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    champLevel = db.Column(db.Integer)
    goldEarend = db.Column(db.Integer)
    goldSpent = db.Column(db.Integer)
    item0_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item1_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item2_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item3_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item4_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item5_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    item6_id = db.Column(db.VARCHAR(20), db.ForeignKey('item.id'))
    itemsPurchased = db.Column(db.Integer)
    longestTimeSpentLiving = db.Column(db.Integer)

    def __init__(self, match_id, champion_id, puuid, participantId,
                isWin, kills, deaths, assists,
                champLevel, goldEarend, goldSpent,
                item0_id, item1_id, item2_id, item3_id,
                item4_id, item5_id, item6_id,
                itemsPurchased, longestTimeSpentLiving):
        self.id = match_id + str(participantId)
        self.match_id = match_id
        self.champion_id = champion_id
        self.puuid = puuid
        self.participantId = participantId
        self.isWin = isWin
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.champLevel = champLevel
        self.goldEarend = goldEarend
        self.goldSpent = goldSpent
        self.item0_id = item0_id
        self.item1_id = item1_id
        self.item2_id = item2_id
        self.item3_id = item3_id
        self.item4_id = item4_id
        self.item5_id = item5_id
        self.item6_id = item6_id
        self.itemsPurchased = itemsPurchased
        self.longestTimeSpentLiving = longestTimeSpentLiving