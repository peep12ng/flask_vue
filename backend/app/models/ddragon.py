from ..extensions import db

class Version(db.Model):
    id = db.Column(db.VARCHAR(10), primary_key=True)
    version = db.Column(db.VARCHAR(10))
    season = db.Column(db.Integer)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)

    _champion = db.relationship('Champion', backref='version')
    _match = db.relationship('Match', backref='version')
    _item = db.relationship('Item', backref='version')
    _perkStyle = db.relationship('PerkStyle', backref='version')
    _perk = db.relationship('Perk', backref='version')
    _spell = db.relationship('Spell', backref='version')

    def __init__(self, id, version, season, num1, num2):
        self.id = id
        self.version = version
        self.season = int(season)
        self.num1 = int(num1)
        self.num2 = int(num2)

class Champion(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(20))
    info = db.Column(db.JSON)
    
    _matchDetail = db.relationship('MatchDetail', backref='champion')

    def __init__(self, id, version_id, key, name, info):
        self.id = id
        self.version_id = version_id
        self.key = key
        self.name = name
        self.info = info
    
class Item(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(150))
    info = db.Column(db.JSON)

    # _matchDetail = db.relationship('MatchDetail', backref='item')

    _matchDetail_item0 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item0_id')
    _matchDetail_item1 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item1_id')
    _matchDetail_item2 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item2_id')
    _matchDetail_item3 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item3_id')
    _matchDetail_item4 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item4_id')
    _matchDetail_item5 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item5_id')
    _matchDetail_item6 = db.relationship('MatchDetail', foreign_keys='MatchDetail.item6_id')

    def __init__(self, id, version_id, key, name, info):
        self.id = id
        self.version_id = version_id
        self.key = key
        self.name = name
        self.info = info

class PerkStyle(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(10))

    _perk = db.relationship('Perk', backref='perk_style')
    _matchDetail_mainPerkStyle = db.relationship('MatchDetail', foreign_keys='MatchDetail.mainPerkStyle_id')
    _matchDetail_subPerkStyle = db.relationship('MatchDetail', foreign_keys='MatchDetail.subPerkStyle_id')

    def __init__(self, id, version_id, key, name):
        self.id = id
        self.version_id = version_id
        self.key = key
        self.name = name

class Perk(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    perkStyle_id = db.Column(db.VARCHAR(20), db.ForeignKey('perk_style.id'))
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    slot = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(20))
    shortDesc = db.Column(db.Text())
    longDesc = db.Column(db.Text())

    _matchDetail_mainPerk1 = db.relationship('MatchDetail', foreign_keys='MatchDetail.mainPerk1_id')
    _matchDetail_mainPerk2 = db.relationship('MatchDetail', foreign_keys='MatchDetail.mainPerk2_id')
    _matchDetail_mainPerk3 = db.relationship('MatchDetail', foreign_keys='MatchDetail.mainPerk3_id')
    _matchDetail_mainPerk4 = db.relationship('MatchDetail', foreign_keys='MatchDetail.mainPerk4_id')
    _matchDetail_subPerk1 = db.relationship('MatchDetail', foreign_keys='MatchDetail.subPerk1_id')
    _matchDetail_subPerk2 = db.relationship('MatchDetail', foreign_keys='MatchDetail.subPerk2_id')

    def __init__(self, id, version_id, key, slot, name, shortDesc, longDesc):
        self.id = id
        self.version_id = version_id
        self.key = key
        self.slot = slot
        self.name = name
        self.shortDesc = shortDesc
        self.longDesc = longDesc

class Shard(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    name = db.Column(db.VARCHAR(10))
    tooltip = db.Column(db.VARCHAR(100))
    shortDesc = db.Column(db.VARCHAR(200))
    longDesc = db.Column(db.VARCHAR(200))
    iconPath = db.Column(db.VARCHAR(100))

    _matchDetail_shardDefense = db.relationship('MatchDetail', foreign_keys='MatchDetail.shardDefense_id')
    _matchDetail_shardFlex = db.relationship('MatchDetail', foreign_keys='MatchDetail.shardFlex_id')
    _matchDetail_shardOffense = db.relationship('MatchDetail', foreign_keys='MatchDetail.shardOffense_id')

    def __init__(self, id, name, tooltip, shortDesc, longDesc, iconPath):
        self.id = id
        self.name = name
        self.tooltip = tooltip
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.iconPath = iconPath

class Spell(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    key = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(100))
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    info = db.Column(db.JSON)

    def __init__(self, id, key, name, version_id, info):
        self.id = id
        self.key = key
        self.name = name
        self.version_id = version_id
        self.info = info