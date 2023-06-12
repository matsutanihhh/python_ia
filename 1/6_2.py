dictionary = {
    'A': 4,
    'B': 10,
    'C': 7,
}

# 指定したキーに対応する値を取得
print(dictionary.get('A'))
# 登録されてないキーを指定すると「None」と返す
print(dictionary.get('D'))