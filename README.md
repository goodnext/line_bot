# 今週の献立リストLINEボット
## 説明
週末に料理をしているが毎週献立を考えるのが大変なので、  
休みの前日の22:00に良さそうな献立をサイトからスクレイピングしてラインにpush通知する  

対象にした献立サイト
- https://www.weekcook.jp/menu/onemenu/dinner/index.html

このサイトにした理由は30分で3品簡単に作れるのが良いなと思ったから。  
夕食をターゲットにしている。

## 概要図
![概要図](https://github.com/goodnext/line_bot/blob/master/img/overview.png?raw=true)

## 基盤
- Heroku
- LINEのMessaging API

## 動作環境
- python3.6
- heroku addon scheduler


## 必要なもの
- Line Developersのアカウント
- LINE@アカウント
- Herokuのアカウント

## ユーザーIDとアクセストークンについて
セキュリティのため環境変数にセット
プログラムでは環境変数の値を参照するようにしている