# セッター・ゲッターのテキストとは異なる記述方法

class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name  # キャラクター名
        self.level = level  # キャラクターレベル
        self.__stamina = level * 20  # 体力
        self.exp = exp  # 経験値
        self.itembox = itembox  # 道具箱

    def attack(self, target):
        """
        攻撃メソッド
        攻撃対象を引数で指定し、相手のスタミナを減らす
        """
        damage = self.level * 5
        print(f'{self.name}の攻撃')
        print(f'{target.name}に{str(damage)}のダメージ\n')
        target.stamina -= damage

    @property
    def stamina(self, new_stamina):
        """
        スタミナのセッター
        体力の最小値は0、最大値はレベル×20
        """
        if new_stamina > self.level * 20:
            self.__stamina = self.level * 20
        elif new_stamina <= 0:
            self.__stamina = 0
            print(f'{self.name}は力尽きた')
        else:
            self.__stamina = new_stamina

    @stamina.setter
    def stamina(self):
        """
        スタミナのゲッター
        """
        return self.__stamina


class Attacker(Character):
    def attack(self, target):
        damage = self.level * 10
        print(f'{self.name}の攻撃')
        print(f'{target.name}に{str(damage)}のダメージ\n')
        target.stamina -= damage


class Healer(Character):
    def healing(self, target):
        recovery_amount = self.level * 5
        print(f'{self.name}は手当てをした')
        print(f'{target.name}の体力が{str(recovery_amount)}回復した\n')
        target.stamina += recovery_amount


taro = Attacker('タロー', 1, 0, {'かいふくやく': 2})
jiro = Healer('ジロー', 1, 0, {'かいふくやく': 2})
enemy = Character('まもの', 1, 0, {})

jiro.attack(enemy)
taro.attack(enemy)
enemy.attack(taro)
jiro.healing(taro)
taro.attack(enemy)

print(taro.stamina)
print(jiro.stamina)
print(enemy.stamina)
