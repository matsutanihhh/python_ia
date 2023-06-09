dic = {
    '商品A': 3,
    '商品B': 10,
    '商品C': 7,
    '商品D': 5}

print('商品一覧')
# keys()メソッドはkeyを取り出して一覧にする
# for key in ['商品A', '商品B', '商品C', '商品D']
# ここではわざわざkeys()メソッドを使わなくてもいい
# for key in dic: でも同じ処理ができる
for key in dic.keys():
    print(key)
# for key in dic: でも同じ処理ができる

print('\n商品と在庫数の一覧')
# items()メソッドでkeyとvalue一度にどちらも取り出せる
for key, value in dic.items():
    print('商品名：' + key + '\t在庫数：' + str(value))


# dic.items()は次のようなリストを作る
tuple_list = [
    ('商品A', 3),
    ('商品D', 10),
    ('商品C', 7),
    ('商品D', 5)
]

for key, value in tuple_list:
    print(key)
    print(value)