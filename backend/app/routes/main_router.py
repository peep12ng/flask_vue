from flask import Blueprint, jsonify, request, make_response
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

@bp.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        print(data)
        print(data['value'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('name')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('value')
        print(user)
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('value')
        print(user)

    return make_response(jsonify({'status': True}), 200)

@bp.route("/search", methods=['GET'])
def search():
    if request.method == 'GET':
        user = request.args.get('name')
        print(user)

    return make_response(jsonify({'status': True}), 200)