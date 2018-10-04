import requests
import json
from bs4 import BeautifulSoup
import datetime
import jpholiday
import os

#push通知するリンク先URL
BASE_URL = 'https://www.weekcook.jp/menu/onemenu/dinner/'

def line_push(messeage):
    url = 'https://api.line.me/v2/bot/message/push'

    data = {
        "to": os.environ["LINE_USER_ID"],
        "messages": [
            {
                "type": "text",
                "text": messeage
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.environ["LINE_ACCESS_TOKEN"]
    }
    requests.post(url, data=json.dumps(data), headers=headers)

def exec_scraping():
    target_url = BASE_URL + 'index.html'
    r = requests.get(target_url)         #requestsを使って、webから取得
    soup = BeautifulSoup(r.text, 'lxml') #html取得

    #献立のリンクの配列
    menu_list = []
    #対象のaタグをループする
    for a in soup.find_all("a", attrs={"class": "btn btn_17 btn_more"}): 
        #配列に追加
        menu_list.append(a.get('href'))
    return menu_list

def get_holiday_list():
    #現在日時のオブジェクトを取得
    now = datetime.datetime.now()
    #休日格納用配列
    holiday_list = []
    #現在年の祝日ループし取得
    for holday in jpholiday.year_holidays(now.year): 
        holiday_list.append(holday[0])

    # 現在日取得
    today = datetime.date.today()
    #　現在日から10日分ループ
    for cnt in range(1, 10):
        cale_date = datetime.timedelta(days=cnt)
        add_date = today + cale_date
        #土曜日または日曜日の場合 休日の配列に格納
        if add_date.weekday() == 5 or add_date.weekday() == 6:
            holiday_list.append(add_date)
    
    #重複を削除
    holiday_list_uniq = list(set(holiday_list))
    #配列のソートする
    holiday_list_uniq.sort()

    return(holiday_list_uniq)

def get_holiday_match_cnt(holiday_list_uniq):
    #休日にマッチした件数
    match_cnt = 0
    #現在日取得
    today = datetime.date.today()
    if today in holiday_list_uniq:
        return(match_cnt)
    
    #現在日から10日分ループ
    for cnt in range(1, 10):
        cale_date = datetime.timedelta(days=cnt)
        # cale_date = datetime.timedelta(days=6)
        next_date  = today + cale_date
        #次の日付が一致した場合もう一度ループ
        if next_date in holiday_list_uniq:
            match_cnt += 1
            continue
        #一致しない場合はループぬける
        else:
            break
    return(match_cnt)

def main():
    #対象のサイトからリンク先取得
    menu_list = exec_scraping()
    #休日のリスト取得
    holiday_list_uniq = get_holiday_list()

    match_cnt = get_holiday_match_cnt(holiday_list_uniq)
    
    if match_cnt > 0:
        line_push('今週の献立リスト')
    for cnt in range(0, match_cnt):
        line_push(BASE_URL + menu_list[cnt])
    

if __name__ == "__main__":
    main()
