yes = 'да'
no = 'нет'
first_q = input("Собака короткошерстрой породы?")
if first_q.lower() == yes:
    second_q = input("Рост собаки менее 50 см?")
    if second_q.lower() == yes:
        third_q = input("У собаки короткий хвост?")
        if third_q.lower() == yes:
            print("английский бульдог")
        elif third_q.lower() == no:
            fifth_q = input("У собаки длинные уши?")
            if fifth_q.lower() == yes:
                print('гончая')
            elif fifth_q.lower() == no:
                sixth_q = input('У собаки короткое тело?')
                if sixth_q.lower() == yes:
                    print('мопс')
                else:
                    print('чихуахуа')
    elif second_q.lower() == no:
        seventh_q = input("Собака весит более 50 кг?")
        if seventh_q.lower() == yes:
            print('датский дог')
        else:
            print('фоксхаунд')
elif first_q.lower() == no:
    second_q = input("Рост собаки менее 50 см?")
    if second_q.lower() == yes:
        eighth_q = input('У собаки доброжелательный характер?')
        if eighth_q.lower() == no:
            print('ирландский сеттер')
        else:
            print('кокер-спаниэль')
    else:
        nineth_q = input("У собаки рост менее 70 см?")
        if nineth_q.lower() == yes:
            fifth_q = input("У собаки длинные уши?")
            if fifth_q.lower() == yes:
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            tenth_q = input("Окрас с белыми отметинами?")
            if tenth_q.lower() == yes:
                print('сенбернар')
            else:
                eleventh_q = input("белоснежный окрас?")
                if eleventh_q.lower() == yes:
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')