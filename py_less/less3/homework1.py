print('pastrami больше нет!')
sandwich_orders = ['pastrami', 'Гамбургер', 'Панини', 'pastrami', 'Крок-мадам', 'Бокадильо', 
                'крок-месье', 'Рубен', 'pastrami', 'Монте-Кристо', 'BLT', 'Дэгвуд' ] 
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_type = sandwich_orders.pop()
    print(f"Твой сендвич {sandwich_type} готов!")
    finished_sandwiches.append(sandwich_type)

print("\nГотовые сендвичи:")
for i in finished_sandwiches:
    print(i)
