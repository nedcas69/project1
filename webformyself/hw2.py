import random


r = random.randint(1,100)

print("Угадай число от 1 до 100!")
bul = True
cnt = 0
while bul:
    user_input = int(input('Введите число: '))
    cnt += 1
    if user_input > r:
        print('Ваше число больше! Попробуйте ещё раз.')
    elif user_input < r:
        print('Ваше число меньше! Попробуйте ещё раз.')
    elif user_input == r:
        print('Вы угадали поздравляем!')
        print(f'Вы отгадали с {cnt} попыток.')
        bul = False
    
