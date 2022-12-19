# def odd_ball(arr):
#     if arr.index('odd') in arr:
#         return True
#     else:
#         return False
#
# print(odd_ball(['even',7,'odd',2,'even',5,6,7,'even']))
# print(odd_ball(['even',7,6,7,'odd',2,'even',5,6,7,'even']))
# print(odd_ball(['even',7,6,7,'odd',2,'even',5,6,7,'even',4]))


# def find_sum(n):
#     s = 0
#     n +=1
#     for i in range(n):
#         if i % 5 == 0 or i % 3 == 0:
#
#             s += i
#
#
#     return s
#
# def find_sum(n):
#
#     return sum(i for i in range(n+1) if i%3==0 or i%5==0)
#
# print(find_sum(10))


# def get_names(l):
#     new_list = []
#     for item in l:
#         if len(item) == 4:
#             new_list.append(item)
#     return new_list
#
# def get_names(names):
#     return [i for i in names if len(i) == 4]
#
# lists = ['Jamshid', 'John', 'Murodjon', 'Mark', 'Shaxboz', 'Ryan', 'Ibrohim', 'Paul']
# print(lists)
# print(get_names(lists))
