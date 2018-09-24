import requests
import json

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
    }
    requests.post(url, data=json.dumps(data), headers=headers)

def main():
    #プッシュ通知をする
    line_push("あいう\nかきく")

if __name__ == "__main__":
    main()
