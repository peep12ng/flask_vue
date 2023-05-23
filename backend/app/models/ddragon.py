from ..extensions import db

class Version(db.Model):
    id = db.Column(db.VARCHAR(10), primary_key=True)
    version = db.Column(db.VARCHAR(50))
    season = db.Column(db.Integer)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)

    _champion = db.relationship('Champion', backref='version')
    _match = db.relationship('Match', backref='version')
    _item = db.relationship('Item', backref='version')
    _perkStyle = db.relationship('PerkStyle', backref='version')
    _perk = db.relationship('Perk', backref='version')
    _spell = db.relationship('Spell', backref='version')

    def __init__(self, id, version):
        self.id = id
        self.version = version
        self.season = int(version.split('.')[0])
        self.num1 = int(version.split('.')[1])
        self.num2 = int(version.split('.')[2])

class Champion(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    name = db.Column(db.VARCHAR(20))
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    # title = db.Column(db.VARCHAR(20))
    # sprite = db.Column(db.VARCHAR(15))
    # sprite_x = db.Column(db.Integer)
    # sprite_y = db.Column(db.Integer)
    # sprite_w = db.Column(db.Integer)
    # sprite_h = db.Column(db.Integer)
    # mainTag = db.Column(db.VARCHAR(10))
    # subTag = db.Column(db.VARCHAR(10))

    _matchDetail = db.relationship('MatchDetail', backref='champion')

    def __init__(self, id, version_id, name, key):
        self.id = id
        self.name = name
        self.version_id = version_id
        self.key = key
        # self.title = title
        # self.sprite = sprite
        # self.sprite_x = sprite_x
        # self.sprite_y = sprite_y
        # self.sprite_w = sprite_w
        # self.sprite_h = sprite_h
        # self.mainTag = mainTag
        # self.subTag = subTag
    
class Item(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
    key = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(150))
    info = db.Column(db.JSON)

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

    def __init__(self, id, version_id, key, slot, name, shortDesc, longDesc):
        self.id = id
        self.version_id = version_id
        self.key = key
        self.slot = slot
        self.name = name
        self.shortDesc = shortDesc
        self.longDesc = longDesc

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

# class Sprite(db.Model):
#     id = db.Column(db.VARCHAR(20), primary_key=True)
#     name = db.Column(db.VARCHAR(20))
#     version_id = db.Column(db.VARCHAR(20), db.ForeignKey('version.id'))
#     image = db.Column(db.MEDUIMBLOB)

#     def __init__(self, id, name, version_id, image):
#         self.id = id
#         self.name = name
#         self.version_id = version_id
#         self.image = image