number_list = [12, 34, 5, 6, 32, 67, -3 , 14, 35]

for number in number_list:
    if number < 0:
        print('処理を停止しました')
        break
    else:
        print(number)