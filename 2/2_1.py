class Character:
    name = ''
    def sepak(self, comment):
        print(self.name + ':' + comment)

taro = Character()
taro.name = 'タロー'
print(taro.name)