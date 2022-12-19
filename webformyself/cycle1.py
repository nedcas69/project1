# i = 1900

# while i <2023:
#     print(i, end=' ')
#     i += 1
# else:
#     print('\n')
     
# таблица умножений
def tablica(i=10):
    for i in range(1,i):
        for j in range(2,10):
            print(f'{i} * {j} = {i*j}\t')
    
        print('') 

user_input = input('Если хотите введите число до которой будет выводится таблица умножений:  ')
if user_input != '':
    tablica(i=int(user_input)+1)
else:
    tablica()
