# user_file_text = """
# hoge
# fuga
# taro
# ziro
# saburo
# """
# この複数行のテキストを、splitメソッドでリストに分割し、アルファベット順に並び替えます。
# その後、joinメソッドを使い、print関数で
# fuga hoge saburo taro ziro(半角スペースで区切られた文字列)
# と表示するプログラムを作成してください。
# 余裕がある方は
# fuga
# fuga
# saburo
# taro
# ziro
# のように、改行された文字列にしてprintしてください。

user_file_text = """
hoge
fuga
taro
ziro
saburo
"""

# 改行区切りの時は区切り文字指定しなければOK
text_list = user_file_text.split()
text_list.sort()
# print(text_list)
text = ' '.join(text_list)
print(text)

text2 = '\n'.join(text_list)
print(text2)
