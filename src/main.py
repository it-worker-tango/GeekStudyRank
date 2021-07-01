import requests
import json

class GeekRank():

    def __init__(self) -> None:
        
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Referer": "https://time.geekbang.org/",
            "Origin": "https://time.geekbang.org"
        }
        self.url = "https://promotion.geekbang.org/race_rank/activity/rank/list"
        self.rank = None
        self.uid = None
        self.medal = None
        self.score = None
        self.points = None
        self.nick_name = None
        self.user_info = None

    def get_data(self):
        req = requests.post(self.url, headers=self.headers, data={})

        if req.status_code==200:
            return req.text
        return False

    def clear_data(self, js_data):
        info = json.loads(js_data)
        info_data = info['data']
        self.user_info = info_data['user_info']
        return info_data

    def get_nick_name(self, uid):
        for info in self.user_info:
            if info['uid'] == uid:
                return info['nick_name']


if __name__ == "__main__":
    geek = GeekRank()
    js_data = geek.get_data()
    if js_data:
        info_data = geek.clear_data(js_data)

        for rank in info_data['list']:
            rank_index = rank['rank']
            uid = rank['uid']
            medal = rank['medal']
            score = rank['score']
            points = rank['points']
            
            nick_name = geek.get_nick_name(uid)
            print(f"{nick_name}:{rank_index}:{points}")
            print("-" * 50)
