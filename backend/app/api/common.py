def to_dict(objects):
    res = []
    for obj in objects:
        res.append(dict((str(col.name), getattr(obj, col.name)) for col in obj.__table__.columns))

    return res