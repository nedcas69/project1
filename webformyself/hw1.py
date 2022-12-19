# words = ['мадам', 'топот', 'test', 'madam', 'word']
# words_palindrom =[i for i in words if i == i[::-1]]
# for i in words:
#     if i == i[::-1]:
#         words_palindrom.append(i)
    
# print(words_palindrom)


my_str =['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindroms = [i for i in my_str if i.lower().replace(' ', '') == i.lower().replace(' ', '')[::-1] ]
# for i in my_str:
#     if i.lower().replace(' ', '') == i.lower().replace(' ', '')[::-1]:
#         palindroms.append(i)
    

print(palindroms)