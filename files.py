my_file = open("lists.txt", "w+")
my_file.write("Hello list!")
my_file.close()

my_file = open("lists.txt", "a+")
my_file.write("\nHello user!")
my_file.close()

my_file = open("lists.txt", "r+") 
print(my_file.read())
my_file.seek(0)
print(my_file.readlines()) #vozvrawaet kajduyu stroku otdelnym elementon
my_file.close()


with open('lists.txt', mode='r') as f: # читает файл и сам закрывает
    x = f.readlines()

print(x)

with open('lists.txt', mode='a') as f:  # добавляет в файл строку
    f.write('\nhello hello!')

print(x)

with open('lists.txt', mode='r') as f: 
    x = f.readlines()

print(x)


with open('lists2.txt', mode='w') as f:  # создает новый файл и записывает значение
    f.write('dear hello!')

print(x)

