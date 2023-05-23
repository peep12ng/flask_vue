from ..utils.enviroment_variables import getKey
import requests
from ..utils.global_variables import (rtime, stime)
import time

class Requester:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token" : getKey()
        }
    
    def get(self, result, url):
        try:
            r = requests.get(
            url=url,
            headers=self.headers
            )
            time.sleep(rtime)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Http Error : ", e)
            if r.status_code==400:
                print("Bad request[400]")
                return r.json()
            elif r.status_code==403:
                print("Forbidden[403]")
                return r.json()
            elif r.status_code==429:
                print("Too Many Request[429]")
                time.sleep(stime)
                return self.get(result, url)
            else:
                print("Other Error")
                return r.json()

        if result=='json':
            return r.json()
        elif result=='content':
            return r.content
        elif result=='status_code':
            return r.status_code