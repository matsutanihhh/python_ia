def plus_g(a):
    print('gの値は' + str(g) + 'です')
    b = a + g
    return b

# 関数の外側で定義された変数は関数の中からも参照できる
g = 1
print(plus_g(3))
