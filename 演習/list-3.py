# 演習問題3.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。
# その際appendメソっドではなくinsertメソッドを使ってください。
# そのリストをprint()関数で表示しますが、その際に組み込み関数sortedを使ってソートされて表示するようにしてください。
# （降順、大きい数値が先に表示される）

number_list = []

user_input_number = input()
number_list.insert(0, int(user_input_number))

user_input_number = input()
number_list.insert(1, int(user_input_number))

user_input_number = input()
number_list.insert(2, int(user_input_number))

print(number_list)

sorted_number_list = sorted(number_list, reverse=True)
print(sorted_number_list)