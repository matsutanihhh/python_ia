class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name  # キャラクター名
        self.__level = level  # キャラクターレベル
        self.stamina = level * 20  # 体力
        self.exp = exp  # 経験値
        self.itembox = itembox  # 道具箱

    def level_up(self):
        if self.exp > self.__level * 10:
            self.exp = self.exp - self.__level * 10
            self.__level += 1
            print(f'レベルが{str(self.__level)}に上がった')
            self.level_up()  # 経験値が余る場合のための再帰処理


taro = Character('タロー', 1, 0, {'かいふくやく': 2})
taro.exp = 35
taro.level_up()
print(taro.exp)
