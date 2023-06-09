# 演習問題3.
# 上のプログラムの末尾に1行追加し、辞書のgetメソッドを使い、入力したvalueをprint関数で表示してみましょう。

data_dict = {}

key = input('keyを入力してください > ')  # 辞書のkeyを入力してもらう
value = input('valueを入力してください > ')  # 辞書のvalueを入力してもらう
data_dict[key] = value

print(data_dict)

# 新たに追加した1行
print(data_dict.get(key))