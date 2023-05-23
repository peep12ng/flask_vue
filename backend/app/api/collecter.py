from .requester import Requester
from ..utils.global_variables import (URL_MATCH_DATA, URL_MATCHHISTORY_IDS, URL_PLAYER_DATA_BY_NAME, URL_PLAYER_DATA_BY_PUUID, URL_DDRAGON_LANGUAGES, URL_DDRAGON_VERSIONS, language)

class Collecter:
    def __init__(self):
        self.requester = Requester()
    
    def get_playerDto(self, by, target):
        if by=='name':
            return self.requester.get('json', URL_PLAYER_DATA_BY_NAME + target)
        elif by=='puuid':
            return self.requester.get('json', URL_PLAYER_DATA_BY_PUUID + target)

    def get_matchHistory(self, puuid, start, count):
        return self.requester.get('json', URL_MATCHHISTORY_IDS + puuid + f"/ids?start={start}&count={count}&queue=450")
            
    def get_matchDto(self, matchId):
        return self.requester.get('json', URL_MATCH_DATA + matchId)
    
    def get_matchTimelineDto(self, matchId):
        return self.requester.get('json', URL_MATCH_DATA + matchId + '/timeline')
    
    def get_versions(self):
        return self.requester.get('json', URL_DDRAGON_VERSIONS)
    
    def get_languages(self):
        return self.requester.get('json', URL_DDRAGON_LANGUAGES)
    
    def get_championsSummary(self, version):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json")
    
    def get_championsFull(self, version):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/championFull.json")
    
    def get_championsAdditional(self, version, name):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion/{name}.json")
    
    def get_championSprites(self, version, sprite):
        return self.requester.get('content', f"https://ddragon.leagueoflegends.com/cdn/{version}/img/sprite/{sprite}.png")
    
    def get_championImage(self, version, name):
        return self.requester.get('content', f"http://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{name}.png")
    
    def get_items(self, version):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/item.json")

    def get_itemImage(self, version, key):
        return self.requester.get('content', f"http://ddragon.leagueoflegends.com/cdn/{version}/img/item/{key}.png")
    
    def get_perks(self, version):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/runesReforged.json")
    
    def get_perkIcon(self, src):
        return self.requester.get('content', f"https://ddragon.canisback.com/img/{src}")
    
    def get_spell(self, version):
        return self.requester.get('json', f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/summoner.json")