# with open()とすると、エラーが起きても、必ずファイルを閉じてくれる
# encoding='utf-8'は必ずつける（文字化け防止）
# 読み込んだ時に文字化けしたら'cp932'を指定してみる
with open('sample.txt', 'w', encoding='utf-8') as file:
    file.write('1行目\n')
    file.write('2行目\n')


# with文を使わないなら、つぎのような処理になる...
# file = None
# try:
#     file = open('sample.txt', 'w', encoding='utf-8')
#     # まだたくさん処理があるかも...
# except Exception:
#     # エラーがあった場合の処理
#     pass
# finally:
#     if file:
#         file.close()

with open('sample.txt', 'r', encoding='utf-8') as file:
    # ファイルの読み出し
    # text = file.read()

    # ファイルから1行ずつ読み出す
    for line in file:
        # ファイルの各行には必ず改行があるので
        # print関数のend引数にから文字列を渡して改行を消しておく
        print(line, end='')