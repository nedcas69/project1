import random


r = random.randint(1, 100)

bul = True
cnt = 0
while bul:
    print("Угадай число от 1 до 100!")
    user_input = int(input('Введите число: '))
    cnt += 1
    if user_input > r:
        print('Ваше число больше! Попробуйте ещё раз.')
    elif user_input < r:
        print('Ваше число меньше! Попробуйте ещё раз.')
    elif user_input == r:
        print('Вы угадали поздравляем!')
        print(f'Вы отгадали с {cnt} попыток.')
        user_variant = input('Хотите сыграть ещё?(y/n): ')
        if user_variant == 'y' or user_variant == 'yes':
            bul = True
            cnt = 0
            r = random.randint(1, 100)
        else:
            bul = False
    
