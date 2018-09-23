import requests
import json

url = 'https://api.line.me/v2/bot/message/push'
data = {
    "to": "Your user ID",
    "messages": [
        {
            "type": "text",
            "text": "Hello, user!"
        }
    ]
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + #アクセストークン#
}
requests.post(url, data=json.dumps(data), headers=headers)
