import requests
import json
from bs4 import BeautifulSoup
import datetime

def line_push(messeage):
url = 'https://api.line.me/v2/bot/message/push'

data = {
    "to": "Your user ID",
    "messages": [
        {
            "type": "text",
            "text": messeage
        }
    ]
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + #アクセストークン#
}
requests.post(url, data=json.dumps(data), headers=headers)

def exec_scraping():
    base_url = 'https://www.weekcook.jp/menu/onemenu/dinner/'
    target_url = base_url + 'index.html'
    r = requests.get(target_url)         #requestsを使って、webから取得
    soup = BeautifulSoup(r.text, 'lxml') #html取得

    #献立のリンクの配列
    menu_list = []
    #対象のaタグをループする
    for a in soup.find_all("a", attrs={"class": "btn btn_17 btn_more"}): 
        #配列に追加
        menu_list.append(a.get('href'))
    return menu_list

def main():
    #対象のサイトからリンク先取得
    # menu_list = exec_scraping()
    date = datetime.datetime(2018, 1, 1, 0, 0)
    print(date)


    #プッシュ通知をする
    # line_push("あいう\nかきく")

if __name__ == "__main__":
    main()
