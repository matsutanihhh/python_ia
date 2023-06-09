# 1から100までfor文で繰り返し、
# 3の倍数のときは「Fizz」
# 5の倍数のときは「Buzz」
# 15の倍数のときは「FizzBuzz」
# それ以外は数値を表示するプログラムを作りましょう。
#
# 出力例.
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# for num in range(100):
#     if (num + 1) % 3 == 0:
#         if (num + 1) % 5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif (num + 1) % 5 == 0:
#         print('Buzz')
#     else:
#         print(num + 1)

for num in range(100):
    if (num + 1) % 15 == 0:
        print('FizzBuzz')
    elif (num + 1) % 3 == 0:
        print('Fizz')
    elif (num + 1) % 5 == 0:
        print('Buzz')
    else:
        print(num + 1)