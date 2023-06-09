# 1から100まで繰り返し、
# 素数の数値を表示するプログラムを作成しましょう。


for i in range(1, 101):
    flag = False
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        print(i)


# 素数の判定を、関数を使った場合の例
# def is_prime(number):
#     # 引数のnumberが素数ならTrueを返す
#     for j in range(2, number):
#         # print(f'  j={j}')
#         if i % j == 0:
#             return False
#
#     # 割り切れなかったら（素数じゃなかったら）ここに到達する
#     return True
#
#
# for i in range(2, 101):
#     if is_prime(i):
#         print(i)