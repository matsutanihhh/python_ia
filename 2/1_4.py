# sは仮引数とも呼ぶ
def message(s=None):
    if s is not None:
        print('入力文字列は「' + s + '」です')
    else:
        print('文字列が未入力です')


# 'Hello World'は実引数とも呼ぶ
# 関数呼び出しの際に、引数名=値のように渡すことができる
message('Hello World')
message()
