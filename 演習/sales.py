# # 各月の売上を書いたsales.txtがあります。
# # これを読み込み、
# #
# # 1. 売上の合計
# #
# # 2. 黒字(0以上)の合計
# #
# # 3. 赤字(0より下)の合計
# #
# # を求めるプログラムを作成しましょう。
# # 1つのファイルの中に、全て書きましょう。

# 変数の定義
sales_total = 0 # 売上合計を計算する変数
sales_plus = 0 # 黒字合計を計算する変数
sales_minus = 0 # 赤字合計を計算する変数

# ファイルを開く
with open('sales.txt', 'r', encoding='utf-8') as file:
    # 各売上の値を1つずつ見ていく
    for row in file:
        # salesに各売上の値を代入
        sales = int(row)

        # 売上合計の計算
        sales_total += int(row)

        # 黒字のとき
        if sales >= 0:
            sales_plus += sales
        # 赤字のとき
        else:
            sales_minus += sales
# 結果の表示
print(sales_total, sales_plus, sales_minus)