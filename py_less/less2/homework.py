while True:
    print("Вход в кинотеатр до 3 лет бесплатно \nот 3 до 12 - 10$ \nот 12 - 15$")
    q = input('Для выхода нажмите \'q\' Введите ваш возраст: ')
    if q != 'q':
        age = int(q)
        if age <= 3:
            print('вход бесплатно')
        elif age > 3 and age <= 12:
            print('ваш билет стоит 10$')
        elif age > 12:
            print('ваш билет стоит 15$')
    else:
        break