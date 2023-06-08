# 演習問題2.
# 空のリストを定義し、組み込み関数input()を3回呼び出して数値を入力し、空のリストに数値を追加してください。
# そのリストをprint()関数で表示しますが、その際に sortメソッドを使ってソートされて表示するようにしてください。
# （昇順、小さい数値が先に表示される）

number_list = []

user_input_number = input()
number_list.append(int(user_input_number))

user_input_number = input()
number_list.append(int(user_input_number))

user_input_number = input()
number_list.append(int(user_input_number))

number_list.sort()
print(number_list)
