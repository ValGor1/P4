first_q = input("Здравтсвуйте! Как Вас зовут?")
print('Очень приятно, ', first_q,'! ','Меня зовут Валера.', sep='')
second_q = int(input("Сколько вам лет?"))
age = 24
dif1 = second_q - age
dif2 = age - second_q
if second_q > age:
    print('Да,', first_q,' Вы старше меня на ', dif1,' лет.' , sep='')
else:
    print('Да,', first_q,' я старше Вас на ', dif2,' лет.' , sep='')
third_q = input('Вам нравится программировать?')
yes = 'да'
no = 'нет'
if third_q.lower() == yes:
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
elif third_q.lower() == no:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')
else:
    print('Только да или нет. Программа очень простая')
