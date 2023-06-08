# 演習1
# 組み込み関数input()を使い、名前を入力してエンターを押すと、
# 「こんにちは、{入力した名前}」
# と表示されるプログラムを作って実行してみましょう。

user_name = input()
print('こんにちは、' + user_name)

# user_name = input()
# result = 'こんにちは、' + user_name

# ちょい古い書き方
# formatで、変数を埋め込める
# 'こんにちは{}'.format(user_name)
# 最近の書き方
# f'hogehoge{変数名}'
# result = f'こんにちは、{user_name}'

# print(result)