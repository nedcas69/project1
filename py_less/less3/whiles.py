# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())