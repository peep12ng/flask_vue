from ..models import Champion, Version, Item, PerkStyle, Perk, Spell, Shard
from .collecter import Collecter
from ..extensions import db
import json

collecter = Collecter()

def add_version(season, num1, num2):
    versionId = str(season) + '0' * (2-len(str(num1))) + '0' * (2-len(str(num2)))
    print(versionId)
    version = f'{season}.{num1}.{num2}'
    newVersion = Version(versionId, version, season, num1, num2)
    
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
    add_shards()

def isinDB_version(season, num1):
    version = Version.query.filter(Version.season==season, Version.num1==num1).first()

    if version!=None:
        return True
    else:
        return False

def add_champions(version):
    champions = collecter.get_championsFull(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for c in champions['data']:

        # Champion
        data = champions['data'][c]
        key = data['key']
        championId = 'C' + version_id + '0' * (4-len(str(key))) + str(key)
        name = data['name']
        champion = Champion(championId, version_id, key, name, data)
        db.session.add(champion)
        db.session.commit()
    
    db.session.close()

def add_items(version):
    items = collecter.get_items(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for i in items['data']:
        if len(i)==4:
            key = i
            data = items['data'][key]
            itemId = 'I' + version_id + str(key)
            item = Item(itemId, version_id, key, data['name'], data)
            db.session.add(item)
            db.session.commit()
    
    blank = Item(f'I{version_id}0000', version_id, 0, '0', '0')
    db.session.add(blank)
    db.session.commit()
    
    db.session.close()

def add_perks(version):
    perks = collecter.get_perks(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for ps in perks:
        key = ps['id']
        perkStyleId = 'PS' + version_id + str(key)
        name = ps['name']

        perkStyle = PerkStyle(perkStyleId, version_id, key, name)
        db.session.add(perkStyle)
        db.session.commit()

        for i, s in enumerate(ps['slots']):
            slot = i+1
            for p in s['runes']:
                key = p['id']
                perkId = 'P' + version_id + str(key)
                perk = Perk(perkId, version_id, key, slot, p['name'], p['shortDesc'], p['longDesc'])
                db.session.add(perk)
                db.session.commit()
        
    db.session.close()

def add_spells(version):
    spells = collecter.get_spell(version)
    version_id = Version.query.filter(Version.version==version).first().id

    for s in spells['data']:        
        key = spells['data'][s]['key']
        id = 'SP' + version_id + '0'*(4-len(key)) + key
        name = spells['data'][s]['name']
        spell = Spell(id, int(key), name, version_id, spells['data'][s])

        db.session.add(spell)
        db.session.commit()

    db.session.close()

def add_shards():
    temp = collecter.get_shard()

    for s in temp:
        if str(s['id']).startswith('5'):
            key = s['id']
            id = 'SH' + str(key)
            name = s['name']
            tooltip = s['tooltip']
            shortDesc = s['shortDesc']
            longDesc = s['longDesc']
            iconPath = f'/meta/images/lol/shard/{key}.png'
            shard = Shard(id, name, tooltip, shortDesc, longDesc, iconPath)
            db.session.add(shard)
            db.session.commit()
    
    db.session.close()