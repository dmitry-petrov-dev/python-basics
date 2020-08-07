# 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.


name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
if age < 30 and 50 <= weight <= 120:
    print(f"{name} {surname}, your are good condition")
elif weight < 50 or weight > 120:
    if 30 <= age < 40:
        print(f"{name} {surname}, your need sport")
    elif age >= 40:
        print(f"{name} {surname}, your need go to doctor")
    else:
        print("Other conditions")
else:
    print("Something wrong")