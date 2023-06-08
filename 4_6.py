food_list = ['ra-men', 'sushi', 'kare-']
food_list2 = food_list


food_list.sort()
# 共有リファレンスを使うと、共有先の変数を参照してもソートの影響が出る
print(food_list2)

# 中身が全く同じリストを用意しソート
food_list3 = ['ra-men', 'sushi', 'kare-']
food_list3.sort()

# リスト内の要素が全て同じ値のためTrueと出力
print(food_list == food_list2)
print(food_list == food_list3)

# 同じオブジェクトであればTrue、違うオブジェクトであればFalse
print(food_list is food_list2)
print(food_list is food_list3)

