from flask import Blueprint, jsonify, request, make_response
from ..api import Collecter, riotapi
from ..api.common import to_dict

from ..models import MatchDetail, Match, Summoner

collecter = Collecter()

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':

        name = request.args.get('name')
        print(name)
        puuid = ''
        isinAPI_summoner = riotapi.get_isinAPI_summoner(name)
        # 1. API에 존재하는 경우        
        if isinAPI_summoner==True:
            puuid = collecter.get_summonerDto('name', name)['puuid']
            isinDB_summoner = riotapi.get_isinDB_summoner(puuid)
            # 1-2. DB에 존재하는 경우
            if isinDB_summoner==True:
                # 1-2-1. 최신 DTO로 업데이트
                riotapi.update_summoner_info(puuid)
            else:
                # 1-2-2. DTO 추가
                riotapi.add_summoner(puuid)

        # 2. 입력 소환사 test update(match 5개)
        riotapi.test_update(puuid)

        # 3. puuid 최근 5개 게임 dict으로 리턴
        result = []
        matchDetails = MatchDetail.query.filter(MatchDetail.puuid==puuid).all()

        for matchDetail in matchDetails:
            d = {}
            d['match_id'] = matchDetail.match_id
            matchTemp = Match.query.filter(Match.id==d['match_id']).first()
            d['gameStartTimeStamp'] = matchTemp.gameStartTimeStamp
            d['gameDuration'] = matchTemp.gameDuration
            d['myData'] = to_dict(matchDetail)
            d['participants'] = to_dict(MatchDetail.query.filter(MatchDetail.match_id==d['match_id']).all())
            result.append(d)
    
    return make_response(jsonify(result), 200)

@bp.route("/test/<name>", methods=['GET'])
def test(name):
    if request.method=='GET':
        
        result = []

        puuid = Summoner.query.filter(Summoner.name==name).first().puuid
        matchDetails = MatchDetail.query.filter(MatchDetail.puuid==puuid).all()

        for matchDetail in matchDetails:
            d = {}
            d['match_id'] = matchDetail.match_id
            matchTemp = Match.query.filter(Match.id==d['match_id']).first()
            d['gameStartTimeStamp'] = matchTemp.gameStartTimeStamp
            d['gameDuration'] = matchTemp.gameDuration
            d['myData'] = to_dict(matchDetail)
            d['participants'] = to_dict(MatchDetail.query.filter(MatchDetail.match_id==d['match_id']).all())
            result.append(d)

    return make_response(jsonify(result), 200)

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