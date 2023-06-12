# 各月の売上を書いたsales.txtがあります。
# これを読み込み、
#
# 1. 売上の合計
#
# 2. 黒字(0以上)の合計
#
# 3. 赤字(0より下)の合計
#
# を求めるプログラムを作成しましょう。
# 1つのファイルの中に、全て書きましょう。


# 今までに書いた3つの処理を、それぞれ関数にし、呼び出しましょう。
#
# total_sales = get_total_sales('sales.txt')
# total_surplus = get_total_surplus('sales.txt')
# total_deficit = get_total_deficit('sales.txt')
# print(total_sales, total_surplus, total_deficit )

# これらをクラスにまとめる
# これは一例
# class SalesForText:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.lines = []
#         # ファイルの容量が少ない場合、
#         # コンストラクタでファイルを読み込んでデータを配列に格納して仕舞えば
#         # 重複するコードが減らせる
#         with open(self.file_name, 'r', encoding='utf-8') as file:
#             for row in file:
#                 self.lines.append(row)
#
#     def get_total_sales(self):
#         """売上の合計を返す関数"""
#         total_sales = 0
#         for line in self.lines:
#             total_sales += int(line)
#         return total_sales
#
#     def get_total_surplus(self):
#         """黒字の合計を返す関数"""
#         sales_plus = 0
#         for line in self.lines:
#             if int(line) >= 0:
#                 sales_plus += int(line)
#         return sales_plus
#
#     def get_total_deficit(self):
#         """赤字の合計を返す関数"""
#         sales_minus = 0
#         for line in self.lines:
#             if int(line) < 0:
#                 sales_minus += int(line)
#         return sales_minus


# 以上をクラス化してみる

import csv


class SalesForText:
    """テキストファイルのデータから売上に関する計算を行うクラス"""

    def __init__(self, file_name):
        """コンストラクタ"""
        # nameを設定する
        self.file_name = file_name

    def get_data_length(self):
        """要素数を返す関数"""
        count = 0
        # ファイルを開く
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                count += 1
        return count


    def get_total_sales(self):
        """売上の合計を返す"""
        sales_total = 0 # 売上合計用変数
        # ファイルを開く
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # 各行ごとにデータ処理
            for row in file:
                # 文字列を数値に変換
                sales = int(row)
                # 売上合計用変数に足していく
                sales_total += sales
        return sales_total

    def get_total_surplus(self):
        """黒字の合計を返す"""
        sales_plus = 0 # 黒字合計用変数
        # ファイルを開く
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # 各行ごとにデータ処理
            for row in file:
                # 文字列を数値に変換
                sales = int(row)
                # 売上が黒字だったら黒字合計用変数に足していく
                if sales >= 0:
                    sales_plus += sales
        return sales_plus

    def get_total_deficit(self):
        """赤字の合計を返す"""
        sales_minus = 0 # 赤字合計用変数
        # ファイルを開く
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # 各行ごとにデータ処理
            for row in file:
                # 文字列を数値に変換
                sales = int(row)
                # 売上が赤字だったら赤字合計用変数に足していく
                if sales < 0:
                    sales_minus += sales
        return sales_minus


# 計算
# sales = SalesForText('sales.txt')
# total_sales = sales.get_total_sales()
# total_surplus = sales.get_total_surplus()
# total_deficit = sales.get_total_deficit()
# print(total_sales, total_surplus, total_deficit)


# 各月の売上を書いたsales.csvがあります。
# 1列目は年、2列目は月、3列目は売上、4列目は主な売上担当者という形式です。
# SalesForTextクラスを継承し、SalesForCSVクラスを作り、
# 3つのメソッドを上書きし、CSVデータから売上、黒字合計、赤字合計を取得できるようにしてください。

class SalesForCSV(SalesForText):
    """CSVファイルのデータから売上に関する計算を行うクラス(SalesForTextを継承)"""

    def get_total_sales(self):
        """売上の合計を返す(オーバーライド)"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # csvファイルの読み込み
            reader = csv.reader(file)
            for row in reader:
                # 各行リストで取ってくる
                # 売上を文字列から数値に変換
                sales = int(row[2])
                sales_total += sales
        return sales_total

    def get_total_surplus(self):
        """黒字の合計を返す(オーバーライド)"""
        sales_plus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # csvファイルの読み込み
            reader = csv.reader(file)
            for row in reader:
                # 売上を文字列から数値に変換
                sales = int(row[2])
                if sales >= 0:
                    sales_plus += sales
        return sales_plus

    def get_total_deficit(self):
        """赤字の合計を返す(オーバーライド)"""
        sales_minus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # csvファイルの読み込み
            reader = csv.reader(file)
            for row in reader:
                # 売上を文字列から数値に変換
                sales = int(row[2])
                if sales < 0:
                    sales_minus += sales
        return sales_minus


# SalesForCSVクラスのインスタンス化
csv_sales = SalesForCSV('sales.csv')

# 各種メソッド呼び出し
total_sales = csv_sales.get_total_sales()
total_surplus = csv_sales.get_total_surplus()
total_deficit = csv_sales.get_total_deficit()
count = csv_sales.get_data_length()


# 結果の表示
print(f'売上合計：{total_sales}円, 黒字合計：{total_surplus}円, 赤字合計：{total_deficit}円')
print(f'件数：{count}')
