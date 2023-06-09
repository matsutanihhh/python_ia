# グローバル変数
a = 7


def sample():
    # グローバル変数の宣言
    global a
    a = 1


sample()
print(a)
