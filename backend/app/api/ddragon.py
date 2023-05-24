from ..models import Champion, Version, Item, PerkStyle, Perk, Spell
from .collecter import Collecter
from ..extensions import db

collecter = Collecter()

def add_version(season, num1):
    version = season + '.' + num1 + '.1'
    id = ''.join('0'+i if len(i)==1 else i for i in version.split('.'))

    newVersion = Version(id, version)
    
    db.session.add(newVersion)
    db.session.commit()
    db.session.close()
    print(f'add version {version}')

    # add assets
    add_champions(version)
    print(f'add champions v{version}')
    add_items(version)
    print(f'add items v{version}')
    add_perks(version)
    print(f'add perks v{version}')
    add_spells(version)
    print(f'add spells v{version}')

    db.session.commit()
    db.session.close()

def isinDB_version(season, num1):

    if len(Version.query.filter(Version.season==season, Version.num1==num1).all())==0:
        return False
    else:
        return True

def add_champions(version):
    champions = collecter.get_championsSummary(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for c in champions['data']:
        data = champions['data'][c]
        key = data['key']
        id = 'C' + version_id + '0'*(4-len(key)) + key
        name = data['name']
        # title = data['title']
        # sprite = data['image']['sprite']
        # sprite_x = data['image']['x']
        # sprite_y = data['image']['y']
        # sprite_w = data['image']['w']
        # sprite_h = data['image']['h']
        # mainTag = data['tags'][0]
        # subTag = data['tags'][1]
        
        # champion = Champion(id, version_id, name, key, title, sprite, sprite_x, sprite_y, sprite_w, sprite_h, mainTag, subTag)
        champion = Champion(id, version_id, name, key)
        db.session.add(champion)
        db.session.commit()
    
    db.session.close()

def add_items(version):
    items = collecter.get_items(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for i in items['data']:
        if len(i)==4:
            id = 'I' + version_id + i
        
            item = Item(id, version_id, i, items['data'][i]['name'], items['data'][i])
            db.session.add(item)
            db.session.commit()
    
    blank = Item('0', version_id, 0, '0', '0')
    db.session.add(blank)
    db.session.commit()
    
    db.session.close()

def add_perks(version):
    perks = collecter.get_perks(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for ps in perks:
        perkStyle_id = 'PS' + version_id + str(ps['id'])
        name = ps['name']

        perkStyle = PerkStyle(perkStyle_id, version_id, ps['id'], name)
        db.session.add(perkStyle)
        db.session.commit()

        for i, s in enumerate(ps['slots']):
            slot = i+1
            for p in s['runes']:
                perk_id = 'P' + version_id + str(p['id'])
                perk = Perk(perk_id, version_id, p['id'], slot, p['name'], p['shortDesc'], p['longDesc'])
                db.session.add(perk)
                db.session.commit()
        
    db.session.close()

def add_spells(version):
    spells = collecter.get_spell(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for s in spells['data']:
        key = spells['data'][s]['key']
        spell_id = 'S' + version_id + '0'*(4-len(key)) + key
        name = spells['data'][s]['name']
        spell = Spell(spell_id, int(key), name, version_id, spells['data'][s])

        db.session.add(spell)
        db.session.commit()

    db.session.close()