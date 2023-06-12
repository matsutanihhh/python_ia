# 関数の演習1.
# 以前作ったFizzBuzzのプログラムを改良し、
# fizzbuzz(1, 100)
# と呼び出すと、1~100までのFizzBuzzが行われるように関数を作成しましょう。
# 上の関数呼び出しの場合は、次のような出力になります。
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# .
# .
# .
def fizzbuzz1(start, end):
    for num in range(start, end + 1):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


print('------演習1------')
fizzbuzz1(1, 100)


# 関数の演習2.
# さらに改良し、次のような呼び出しができるように変更しましょう。
# fizzbuzz()  # 引数を指定しない場合は、自動で1から100までのFizzBuzzとなる
# fizzbuzz(start=10, end=20)

def fizzbuzz2(start=1, end=100):
    # for num in range(start, end + 1):
    #     if num % 15 == 0:
    #         print('FizzBuzz')
    #     elif num % 3 == 0:
    #         print('Fizz')
    #     elif num % 5 == 0:
    #         print('Buzz')
    #     else:
    #         print(num)
    # 上記コメントアウト部分がfizzbuzz1と一緒なので省いた
    fizzbuzz1(start, end)


print('\n------演習2-デフォルト値ver.------')
fizzbuzz2()
print('\n------演習2-(10, 20)ver.------')
fizzbuzz2(10, 20)
