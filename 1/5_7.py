a = ['blue', 'red', 'yellow', 'blue', 'green']
del a[2] # 2番目の要素 yellow を削除
print(a)

a.pop() # 最後の要素 green を削除
print(a)

# remove(要素名)は指定した要素名のうち最初の値を削除
a.remove('blue') # 最初の要素 blue を削除
print(a)
