def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

def build_person(first_name, last_name, age= None):

    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    
    return person

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(f'\n{musician}')

futbolist = build_person(first_name='jo', last_name='hart', age=27)
print(futbolist)

