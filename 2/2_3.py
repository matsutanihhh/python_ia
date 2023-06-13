class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name            # キャラクター名
        self.level = level          # キャラクターレベル
        self.stamina = level * 20   # 体力
        self.exp = exp              # 経験値
        self.itembox = itembox      # 道具箱


taro = Character('タロー', 1, 0, {'かいふくやく': 2})
print(taro.level)
print(taro.itembox['かいふくやく'])