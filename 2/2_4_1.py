class Character:

    def __init__(self, name, level):
        self.name = name
        # levelには、外からアクセスしないで欲しい
        # self._level = level # アンダースコア1つの場合は、アクセスしようと思えばできる
        self.__level = level  # アンダースコア2つの場合は、アクセスできない

    def speak(self):
        print()




taro = Character('タロー', 1)
print(taro.__level)  # エラー出る
