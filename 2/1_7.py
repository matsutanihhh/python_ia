# 消費税の計算
# 関数は消費税額を返す
def tax(price):
    tax = int(price * 0.1)
    return tax


a = tax(75)
b = tax(1980)
print(a)
print(b)
