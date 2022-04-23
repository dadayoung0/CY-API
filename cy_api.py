import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta


class CY_API:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")

    def serch_player_by_nickname(self, nickname):
        url = "https://api.neople.co.kr/cy/players"
        #! TEST DATA
        nickname = os.getenv("NAME")

        params = {
            "nickname": nickname,
            "wordType": "full",  # match: 동일 단어만 / full: 전문 검색(2~8자)
            "limit": 200,  # 0~200
            "apikey": self.api_key,
        }

        res = requests.get(url, params=params).json()["rows"]
        return res

    def get_info_by_player_id(self, player_id):
        #! TEST DATA
        player_id = os.getenv("ID")

        url = "https://api.neople.co.kr/cy/players/" + player_id
        params = {"apikey": self.api_key}

        res = requests.get(url, params=params).json()

        return res

    def get_match_info_by_player_id(self, player_id):
        #! TEST DATA
        player_id = os.getenv("ID")

        url = "https://api.neople.co.kr/cy/players/" + player_id + "/matches"

        now = datetime.now()
        serch_days = timedelta(days=90)
        params = {
            "gameTypeId": "normal",  # rating: 공식 / nomal: 일반
            # Date 형식: 2018-09-01 00:00 / 20180901T0000
            "startDate": (now - serch_days).strftime("%Y-%m-%d %H:%M"),  # 최대 90일
            "endDate": now.strftime("%Y-%m-%d %H:%M"),
            "limit": 200,
            "apikey": self.api_key,
        }

        res = requests.get(url, params=params).json()

        return res


if __name__ == "__main__":
    api = CY_API()
    print(api.get_match_info_by_player_id("ㄴㅇㄹㄴ")["matches"])
