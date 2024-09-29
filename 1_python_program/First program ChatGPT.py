# Функція для додавання двох чисел
def add(x, y):
    return x + y

# Функція для віднімання двох чисел
def subtract(x, y):
    return x - y

# Функція для множення двох чисел
def multiply(x, y):
    return x * y

# Функція для ділення двох чисел
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе!"
    return x / y

# Вибір операції
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

while True:
    # Введення вибору користувача
    choice = input("Введіть номер операції (1/2/3/4): ")

    # Перевірка, чи вибрана операція є дійсною
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        # Запит на нову операцію
        next_calculation = input("Бажаєте виконати ще одну операцію? (так/ні): ")
        if next_calculation.lower() != 'так':
            break
    else:
        print("Неправильний вибір операції!")
