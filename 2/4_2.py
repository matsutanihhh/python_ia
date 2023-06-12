import datetime

# 現在の日付・時刻
now = datetime.datetime.now()
print(now)

# 現在日時から指定した部分だけ取ってくる
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 日時を日本語のフォーマットへ変換(力技)
text = f'{now.year}年{now.month}月{now.day}日　{now.hour}時{now.minute}分{now.second}秒'
print(text)

# 日時を日本語のフォーマットへ変換(メソッドを使って)
text = now.strftime('%Y年%m月%d日 %H時%M分%S秒')
print(text)


# 今日
today = datetime.date.today()
print(today)
