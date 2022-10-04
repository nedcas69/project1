name = "Sam"
#name[0] = "P" не будет работать так как строки не изменны
last_letters = name [1:]
print('P' + last_letters) #конкатенация строк!!!

x = 'Hello world'
x = x + ' it is beautiful outside!\n'
print(x)
x = x.upper()  #заглавные буквы/ lower() все буквы в нижний регистр!
#x = x.split() # разбивает строку на отдельные части. 
# поумолчанию стоить пробел, можно поменять значение
# разделителя на присуствующие в строке буквы или символы
letter = x * 9 # умножение строк

print(letter)

# 2 + 3 = 5
# '2' + '3' = '23'
 

my_name = ' Shax'
hello = 'Hello'
print(hello + my_name)