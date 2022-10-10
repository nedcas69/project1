import random

lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbols= "!@#$%&*()-+*?/"

Use_for = lower_case + upper_case + number + symbols
length_for_password = 8

password = "".join(random.sample(Use_for, length_for_password))

print(f"Ваш сгенерированный пароль: {password}")