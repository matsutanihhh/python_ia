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

# クラス化

class SalesForText:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_total_sales(self):
        """売上の合計を返す"""
        sales_total = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                sales_total += sales
        return sales_total

    def get_total_surplus(self):
        """黒字の合計を返す"""
        sales_plus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                if sales >= 0:
                    sales_plus += sales
        return sales_plus

    def get_total_deficit(self):
        """赤字の合計を返す"""
        sales_minus = 0
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for row in file:
                sales = int(row)
                if sales < 0:
                    sales_minus += sales
        return sales_minus


# 計算
sales = SalesForText('sales.txt')
total_sales = sales.get_total_sales()
total_surplus = sales.get_total_surplus()
total_deficit = sales.get_total_deficit()
print(total_sales, total_surplus, total_deficit)
