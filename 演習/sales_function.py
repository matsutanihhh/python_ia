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

def get_total_sales(file_name):
    """売上の合計を返す関数"""
    total_sales = 0
    # ファイルを開く
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            total_sales += int(line)
    return total_sales


def get_total_surplus(file_name):
    """黒字の合計を返す関数"""
    sales_plus = 0
    # ファイルを開く
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if int(line) >= 0:
                sales_plus += int(line)
    return sales_plus


def get_total_deficit(file_name):
    """赤字の合計を返す関数"""
    sales_minus = 0
    # ファイルを開く
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if int(line) < 0:
                sales_minus += int(line)
    return sales_minus


# 計算
total_sales = get_total_sales('sales.txt')
total_surplus = get_total_surplus('sales.txt')
total_deficit = get_total_deficit('sales.txt')
print(total_sales, total_surplus, total_deficit)

