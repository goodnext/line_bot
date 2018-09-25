import requests
import json
from bs4 import BeautifulSoup

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
    target_url = 'https://www.weekcook.jp/menu/onemenu/dinner/index.html'
    r = requests.get(target_url)         #requestsを使って、webから取得

    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.find_all("a", attrs={"class": "btn btn_17 btn_more"}))

def main():
    exec_scraping()
    #プッシュ通知をする
    # line_push("あいう\nかきく")

if __name__ == "__main__":
    main()
