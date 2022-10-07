#словари используют {'key1':'value1', 'key2':'value2'} нельзя сортировать словари
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])

prices_lookup = {'apple':'7000', 'orange':'25000', 'milk':'4000'}
print(prices_lookup['milk'])

d = {'k1':123, 'k2':[1,2,3,4,5], 'k3':{'insideKey':100}}
print(d['k2'][2  ])
print(d['k3']['insideKey'])

d = {'k1':['a', 'b', 'c']}
d['k2'] = ['d', 'e']
d['k3'] = ['f', 'g']
d['k2'] = 'mount'
print(d['k1'][2].upper())
print(d)
print(d.keys())
print(d.items())
print(d.values())
