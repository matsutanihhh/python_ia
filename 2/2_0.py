class Character:
    name = ''

    # ダンダーイニット、特殊メソッド
    # taro.__init__('hoge')という風に呼び出されることはない
    def __init__(self, name):
        self.name = name

    # strメソッド
    # ダンダーストラ、特殊メソッド
    # 特定の文字列を返すように設定できる
    # 人間が見やすいクラスの文字列表現を返す
    # 主にデバッグで使われる
    def __str__(self):
        return f'{self.name}のインスタンスです'

    # メソッド
    # メソッドの第1引数にはほぼ必ずインスタンス自身が渡される
    def speak(self, comment):
        print(self.name + ':' + comment)


class Healer(Character):
    # pass  # 詳しい中身は書かず、とりあえず定義だけしたい時にpassと記述
    # initのオーバーライド
    def __init__(self, name, power):
        # superを使うと基底クラスのメソッドを呼び出せる
        # super().基底クラスのメソッド名
        super().__init__(name)
        self.power = power

    # メソッドの新規追加
    def healing(self):
        print(f'{self.name}は回復した！')

    # メソッドのオーバーライド
    def speak(self, comment):
        print(self.name + ':' + comment)
        self.healing()


# 親クラスであるCharacterクラスで定義されたメソッド継承している
#
jiro = Healer('jiro', '回復')  # インスタンス化
jiro.speak('ジローだよ')

# Characterクラスのインスタンスを変数taroに代入
# selfとtaroは全く同じもの
taro = Character('taro')  # インスタンス化、クラス名の後の()は必ずつける
taro.speak(comment='ハロー')
print(str(taro))

# インスタンスの属性は基本的にはコンストラクタで行う
# 他のメソッド内からインスタンスの属性を設定することもある
# taro.name = 'ziro' のように外側から設定することは少ない（上書きはできるけど）
# taro.name = 'タロー'
# print(taro.name)
# クラスのデータ属性に無くても、自由に属性を追加できる
# taro.first_name = 'タロー'
# taro.last_name = 'タナカ'
#
# taro.speak(comment='ハロー')
