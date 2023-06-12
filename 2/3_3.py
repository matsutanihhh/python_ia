import csv
# pandas データ処理のライブラリ

# データの読み込み
with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # rowはリストとなっている
        # ['taro', '15', '札幌', 'a@a.com']
        # print(row)

        # 各データの名前だけ取り出して表示
        print(row[0])

# データの書き込み
    # encoding='utf-8-sig'とすると
    # Windowsのエクセルでも
    # 通常のテキストエディタでも
    # 文字化けせずにcsvを表示できる
    with open('data.csv', 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['taro', '15', '札幌', 'a@a.com'])
        writer.writerow(['saburo', '17', '北海道hokkaidou', 'b@a.com'])
        writer.writerow(['ziro', '16', '札幌', 'c@a.com'])
