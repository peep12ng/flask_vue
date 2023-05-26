def to_dict(object):
    if type(object)==list:
        res = []
        for obj in object:
            res.append(dict((str(col.name), getattr(obj, col.name)) for col in obj.__table__.columns))
    else:
            res = {}
            res = dict((str(col.name), getattr(object, col.name)) for col in object.__table__.columns)
    return res