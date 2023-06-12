import datetime

# 年　月　日　時　分　秒
# 2023/6/12 9:00:00
one_day = datetime.datetime(2023, 6, 12, 9, 00, 00)

# 10日後の計算
ten_days_after = one_day + datetime.timedelta(days=10)
print(ten_days_after)

# 日時の入力を受け取り
day_string = input('Y/m/d H:M:S の形式で入力！ >')
# 入力されたそれっぽい文字列からdatetimeオブジェクトを作る
day_dt = datetime.datetime.strptime(day_string, '%Y/%m/%d %H:%M:%S')

# 20日後の計算
days_after_20 = day_dt + datetime.timedelta(days=20)
print(days_after_20)
