class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name  # キャラクター名
        self.__level = level  # キャラクターレベル
        self.__stamina = level * 20  # 体力
        self.exp = exp  # 経験値
        self.itembox = itembox  # 道具箱

    def set_stamina(self, new_stamina):
        """
        スタミナのセッター
        体力の最小値は0、最大値はレベル×20
        """
        if new_stamina > self.__level * 20:
            self.__stamina = self.__level * 20
        elif new_stamina <= 0:
            self.__stamina = 0
            print(f'{self.name}は力尽きた')
        else:
            self.__stamina = new_stamina

    def get_stamina(self):
        """
        スタミナのゲッター
        """
        return self.__stamina

    stamina = property(get_stamina, set_stamina)


taro = Character('タロー', 1, 0, {'かいふくやく': 2})
taro.stamina = 200
print(taro.stamina)
taro.stamina = -10
print(taro.stamina)
