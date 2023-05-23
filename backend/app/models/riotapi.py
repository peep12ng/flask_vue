from ..extensions import db
import datetime

now = datetime.datetime.now()

class User(db.Model):
    puuid = db.Column(db.VARCHAR(100), primary_key=True)
    name = db.Column(db.VARCHAR(20))
    level = db.Column(db.Integer)
    icon_id = db.Column(db.VARCHAR(20))
    create_at = db.Column(db.DateTime, default=now)
    update_at = db.Column(db.DateTime, default=now)

    _matchDetail = db.relationship('MatchDetail', backref='user')

    def __init__(self, puuid, name, level, icon_id):
        self.puuid = puuid
        self.name = name
        self.level = level
        self.icon_id = icon_id

class Match(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    gameVersion = db.Column(db.VARCHAR(30))
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    winTeam = db.Column(db.Integer)

    _matchDetail = db.relationship('MatchDetail', backref='match')

    def __init__(self, id, gameVersion, version_id, winTeam):
        self.id = id
        self.gameVersion = gameVersion
        self.version_id = version_id
        self.winTeam = winTeam

class MatchDetail(db.Model):
    id = db.Column(db.VARCHAR(30), primary_key=True)
    match_id = db.Column(db.VARCHAR(20), db.ForeignKey('match.id'))
    champion_id = db.Column(db.VARCHAR(20), db.ForeignKey('champion.id'))
    puuid = db.Column(db.VARCHAR(100), db.ForeignKey('user.puuid'))

    def __init__(self, id, match_id, champion_id, puuid):
        self.id = id
        self.match_id = match_id
        self.champion_id = champion_id
        self.puuid = puuid