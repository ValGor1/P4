question = str(input("Вы поедете на бал?: "))
first = "да"
second = "нет"
if question.lower() == first or question.lower() == second:
    print("Неверно")
else:
    print("верно")