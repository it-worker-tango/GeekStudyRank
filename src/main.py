import requests


class GeekRank():

    def __init__(self) -> None:
        
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Referer": "https://time.geekbang.org/",
            "Origin": "https://time.geekbang.org"
        }
        self.url = "https://promotion.geekbang.org/race_rank/activity/rank/list"

    def get_data(self):
        req = requests.post(self.url, headers=self.headers, data={})

        if req.status_code==200:
            return req.text
        return False

    def clear_data(self, js_data):
        print(js_data)

if __name__ == "__main__":
    geek = GeekRank()
    js_data = geek.get_data()
    if js_data:
        geek.clear_data(js_data)
