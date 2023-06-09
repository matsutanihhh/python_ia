def cleaning(date, **kwargs):
    place_person = ''
    for place, person in kwargs.items():
        place_person = place_person + place + ':' + person + ' '

    print(date + 'の清掃担当者は ' + place_person + 'です')


cleaning('12月3日', トイレ='山本', 休憩室='三浦')
