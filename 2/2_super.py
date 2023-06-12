class Character:
    name = ''
    age = 0
    speed = 0

    # ダンダーイニット、特殊メソッド
    # taro.__init__('hoge')という風に呼び出されることはない
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

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

    def show_profile(self):
        print(self.name)
        print(self.age)
        print(self.speed)


class Healer(Character):
    # pass  # 詳しい中身は書かず、とりあえず定義だけしたい時にpassと記述
    # initのオーバーライド
    def __init__(self, name, age, speed, heal_power):
        # self.name = name
        # self.age = age
        # self.speed = speed
        # 上の3行は親クラスのコンストラクタで定義されている
        # 子クラスのコンストラクタでもう一度書く必要はない
        # superを使うと基底クラスのメソッドを呼び出せる
        # super().基底クラスのメソッド名
        super().__init__(name, age, speed)
        self.heal_power = heal_power

    # メソッドの新規追加
    def healing(self):
        print(f'{self.name}は回復した！')

    # メソッドのオーバーライド
    def speak(self, comment):
        print(self.name + ':' + comment)
        self.healing()


class Magician(Character):
    def __init__(self, name, age, speed, magic_power):
        super().__init__(name, age, speed)
        self.magic_power = magic_power

    def show_profile(self):
        # print(self.name)
        # print(self.age)
        # print(self.speed)
        # この3行は親クラスのshow_profileメソッドで定義されている
        # 上の3行を書くより下の1行を書くほうが楽だし行数も少なく冗長でない
        super().show_profile()

        # ↓の処理だけ、このクラス独自のもの
        print(self.magic_power)


# 親クラスであるCharacterクラスで定義されたメソッド継承している
#
jiro = Healer('jiro', '回復')  # インスタンス化
jiro.speak('ジローだよ')

# Characterクラスのインスタンスを変数taroに代入
# selfとtaroは全く同じもの
taro = Character('taro')  # インスタンス化、クラス名の後の()は必ずつける
taro.speak(comment='ハロー')
print(str(taro))
