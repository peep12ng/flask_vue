from flask import Blueprint, jsonify
from ..api import Collecter, riotapi

from ..models import MatchDetail

collecter = Collecter()

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main', methods=['GET'])
def main():
    name = '여자맨'
    if riotapi.isinAPI_user(name)==True:
        puuid = collecter.get_playerDto('name', name)['puuid']
        if riotapi.isinDB_user(puuid)==True:
            riotapi.update_user_info(puuid)
        else:
            riotapi.add_user(puuid)

    riotapi.test_update(puuid)

    result = len(MatchDetail.query.filter(MatchDetail.puuid==puuid).all())
    
    data = {"result": result}

    return jsonify(data)