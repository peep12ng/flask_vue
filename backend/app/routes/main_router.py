from flask import Blueprint, jsonify, request, make_response
from ..api import Collecter, riotapi
from ..api.common import to_dict

from ..models import MatchDetail

collecter = Collecter()

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        name = request.args.get('name')
        if riotapi.isinAPI_user(name)==True:
            puuid = collecter.get_playerDto('name', name)['puuid']
            if riotapi.isinDB_user(puuid)==True:
                riotapi.update_user_info(puuid)
            else:
                riotapi.add_user(puuid)

        riotapi.test_update(puuid)
        mds = MatchDetail.query.filter(MatchDetail.puuid==puuid).all()

        data = to_dict(mds)
    
    return make_response(jsonify(data), 200)

# @bp.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
# def test():
#     if request.method == 'POST':
#         print('POST')
#         data = request.get_json()
#         print(data)
#         print(data['value'])
#     if request.method == 'GET':
#         print('GET')
#         user = request.args.get('name')
#         print(user)
#     if request.method == 'PUT':
#         print('PUT')
#         user = request.args.get('value')
#         print(user)
#     if request.method == 'DELETE':
#         print('DELETE')
#         user = request.args.get('value')
#         print(user)

#     return make_response(jsonify({'status': True}), 200)