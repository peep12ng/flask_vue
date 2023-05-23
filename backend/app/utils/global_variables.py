# 서버
region = 'kr'
# 지역
continent = 'asia'

language = 'ko_KR'

URL_PLAYER_DATA_BY_NAME = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

URL_PLAYER_DATA_BY_PUUID = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'

URL_MATCHHISTORY_IDS = f'https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/'

URL_MATCH_DATA = f'https://{continent}.api.riotgames.com/lol/match/v5/matches/'

URL_DDRAGON_LANGUAGES = 'https://ddragon.leagueoflegends.com/cdn/languages.json'

URL_DDRAGON_VERSIONS = 'https://ddragon.leagueoflegends.com/api/versions.json'

QUERY_RANK = ("SELECT * FROM rankTable")

# 요청 속도 제한
rtime = 0.6
# 요청 속도 제한 초과(429) 발생 시 대기 시간
stime = 10