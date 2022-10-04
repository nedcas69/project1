#добавление строк
from unittest import result

name = 'Shax'
print('Эта строка была {}'.format('добавлена!'))
print('У меня есть {} {} {}'.format('вкусное', "красное", "яблоко!"))
print('У меня есть {1} {0} {2}'.format('вкусное', "красное", "яблоко!"))
print('У меня есть {y}, {v} {k}{end}'.format(v='вкусное', k="красное", y="яблоко", end='!'))
print(f'Моё имя {name}')


#форматирование float

result = 1000/45678
print('Результат: {r:2.3f}'.format(r=result))