import requests
import json
import shutil
import random
import sqlite3
import datetime

class GeekRank():

    def __init__(self) -> None:
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Referer": "https://time.geekbang.org/",
            "Origin": "https://time.geekbang.org"
        }
        self.url = "https://promotion.geekbang.org/race_rank/activity/rank/list"

        shutil.copy(f"./template/rangk.html", "./rangk.html")
        self.cx = sqlite3.connect("info.sqlite")
        self.cu = self.cx.cursor()
    
        # sql = "CREATE TABLE info (uid, nick_name, rank_index, points, score, medal, date_str)"
        # self.insert_data(sql)

    

    def insert_data(self, sql):
        self.cu.execute(sql)
        self.cx.commit()
        

    def get_info(self, sql):
        self.cu.execute(sql)
        return self.cu.fetchall()

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


    def replace_info(self, html_file, old_str, new_str):
        temp = ""
        with open(html_file, 'r', encoding="utf-8") as f:
            temp = f.read()
            temp = temp.replace(old_str, new_str)

        with open(html_file, 'w', encoding="utf-8") as f:
            f.write(temp)


        

if __name__ == "__main__":
    geek = GeekRank()
    today = (datetime.datetime.now()- datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    # js_data = geek.get_data()
    # jdData_str = []
    
    # data_str = []#[[x * random.randint(1,3) for x in range(1,52)], [x * random.randint(1,3) for x in range(1,52)]]
    # if js_data:
    #     info_data = geek.clear_data(js_data)
    #     for rank in info_data['list']:
    #         rank_index = rank['rank']
    #         uid = rank['uid']
    #         medal = rank['medal']
    #         score = rank['score']
    #         points = rank['points']
            
    #         nick_name = geek.get_nick_name(uid)
    #         jdData_str.append(nick_name)
    #         data_str.append(points)
    #         sql = f"INSERT INTO info values('{uid}','{nick_name}','{rank_index}','{points}','{score}','{medal}','{today}')"
    #         geek.insert_data(sql)
        
    #     temp = jdData_str[:50]
    #     jdData_str = []
    #     jdData_str.append(temp)
    #     jdData_str.append(temp)
    #     jdData_str.append(temp)
    #     temp = data_str
    #     data_str = []
    #     data_str = [[x * random.randint(1,3) for x in range(1,52)], [x * random.randint(1,3) for x in range(1,52)]]
    #     data_str.append(temp[:50])
    #     print(jdData_str)
    #     print(data_str)
    date_temp = datetime.date.today()
    years_str = [f"{date_temp.year}-0{date_temp.month}-0{x}" for x in range(1, date_temp.day)]
    infos = geek.get_info(f"select * from info order by date_str")
    
    jdData_str = []
    ifno_data = {}
    for i in years_str:
        ifno_data[i] = {"name":[],"rank":[]}

    for info in infos:
        ifno_data[info[6]]['name'].append(info[1])
        ifno_data[info[6]]['rank'].append(info[3])

    data_str = []
    jdData_str = []
    print(years_str)
    print(ifno_data)
    for i in years_str:
        data_str.append(ifno_data[i]['rank'][:20])
        jdData_str.append(ifno_data[i]['name'][:20])
    print(jdData_str)
    print(data_str)
    geek.replace_info("rangk.html","years_str", f"{years_str}")
    geek.replace_info("rangk.html","jdData_str", str(jdData_str[:30]))
    geek.replace_info("rangk.html","data_str", str(data_str[:30]))
    # geek.cx.close()
