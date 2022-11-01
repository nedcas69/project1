'''
def describe_pet(animal_type, pet_name): #Позиционные аргументы
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


def describe_pet(animal_type, pet_name): #Именованные аргументы
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='milly')
'''
def describe_pet(pet_name, animal_type='dog'): #Значения по умолчанию
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')
describe_pet(animal_type='hamster', pet_name='harry')