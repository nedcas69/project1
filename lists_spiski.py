my_list = [1, 2, 3] #список целых чисел
my_list = ['string', 100, 21.08] #список значений
print(len(my_list))

my_list = ['one', 'two', 'three']
print(my_list[0])
print(my_list[1:])

another_list = ['four', 'five']
konkaten_list = my_list + another_list #конкатенация списков
print(konkaten_list)

konkaten_list[0] = 'ONE' #замена элемента
print(konkaten_list)

konkaten_list.append('six')   # добавление в конец списка
print(konkaten_list)

new_list = konkaten_list
pelement = new_list.pop()      #удаление элемента  и возврашение 
#(поумолчанию pop(-1)) усли pop(0) то значение будет ONE
#new_list.sort() сортирует содержимое списка
#new_list.reverse() переводит в обратный порядок
print(new_list)
print(pelement)


