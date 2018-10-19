# memo

### 仮想環境の作成
```
virtualenv line_bot_py
```

### 仮想環境の有効化
```
source line_bot_py/bin/activate
```

(line_bot_py) が表示されればオッケー

### 仮想環境の無効化
```
deactivate
```

### モジュールインストール
```
pip install beautifulsoup4
pip install lxml
pip install jpholiday
```

https://devcenter.heroku.com/articles/getting-started-with-python#set-up
ここからmacのheroku cliをインストール

- herokuに環境変数をセットする
heroku config:set LINE_USER_ID=*** LINE_ACCESS_TOKEN=***

- モジュールをテキストにする
pip freeze > requirements.txt

herokuのタイムゾーンを変更する
heroku run bash　-a app_name

これでbashでログインできる
dateで確認
>Mon Nov 21 02:35:04 UTC 2016

exit

heroku config:add TZ=Asia/Tokyo -a app_name

変更されているか確認

herokuのアドオン追加

heroku addons:add scheduler:standard 


