dictionary = {
    'A': 3,
    'B': 10,
    'C': 7,
    'D': 5
}

# キーを指定して削除
del dictionary['C']
print(dictionary)

# キーを指定して削除
# その際、削除した値を返す
a = dictionary.pop('B')
print(a)
print(dictionary)