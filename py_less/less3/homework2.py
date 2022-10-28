responses = {}
polling_active = True
while polling_active:
    name = input('Как вас зовут?: ')
    response = input('Где бы вы хотели отдохнуть в этот отпуск?: ')
    responses[name] = response
    yes_no = input('Продолжить опрос? (yes/no)')
    if yes_no == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} хотел бы отдохнуть в {response}.")