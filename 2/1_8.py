# 戻り値が複数
def tax(price):
    tax = int(price * 0.1)
    price_including_tax = int(price * 1.1)
    # 戻り値が複数の時はタプルとして返している
    return (price_including_tax, tax)


# 複数の戻り値を受け取るため2つの変数を用意することもできる
# 1つだけ用意するとタプルが代入される
a, b = tax(100)
print(a)
print(b)
