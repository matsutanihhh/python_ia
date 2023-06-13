import datetime
one_day = datetime.datetime(2023, 6, 13, 10, 30, 00)
ten_days_after = one_day + datetime.timedelta(days=10)

comparison = one_day < ten_days_after
print(comparison)