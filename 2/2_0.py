class Character:
    name = ''

    # ダンダーイニット、特殊メソッド
    # taro.__init__('hoge')という風に呼び出されることはない
    def __init__(self, name):
        self.name = name

    # メソッド
    # メソッドの第1引数にはほぼ必ずインスタンス自身が渡される
    def speak(self, comment):
        print(self.name + ':' + comment)


# Characterクラスのインスタンスを変数taroに代入
# selfとtaroは全く同じもの
taro = Character('tarou')  # インスタンス化、クラス名の後の()は必ずつける
taro.speak(comment='ハロー')

# インスタンスの属性は基本的にはコンストラクタで行う
# 他のメソッド内からインスタンスの属性を設定することもある
# taro.name = 'ziro' のように外側から設定することは少ない（上書きはできるけど）
taro.name = 'タロー'
print(taro.name)
# クラスのデータ属性に無くても、自由に属性を追加できる
taro.first_name = 'タロー'
taro.last_name = 'タナカ'

taro.speak(comment='ハロー')
