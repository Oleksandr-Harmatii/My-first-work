# Звіт до роботи
## Тема: Основи програмування на Python
### Мета роботи: Навчитись основам програмування на Python

---
### Виконання роботи
* Результати виконання завдання *1...N*;
    1. Я ознайомився з основами типів даних, дізнавшись всі їхні види, а  також використавши приклад, який знаходиться в окремому файлі: 
    ```Python
    a = "змінна з текстом"  
    b = 1                   
    b1 = 1.1                
    c = ["a", 1, 1.25, "Слово", a]  
    d = {"a": "Слово", "b": 1, a: b} 
    e = ("a", a)            
    f = {"ss", a}     
    ```
    1. В другому завданні, я дізнався про різні вбудовані константи, в окремому файлі я використав три вида, один з яких вставляю тут:
    ```Python
    result = None  
    print("Значення змінної result:", result)  

    def my_function():
        return None

    print("Результат функції my_function:", my_function())  # Виведе: Результат функції my_function: None
    ```
    1. В третьому завданні, я попрактикувався з вбудованими функціями, і зрозумів наскільки вони корисні, наприклад функція len(), або ж max() і min(), якщо так задуматись вони дуже корисні в подальшому для програмування, так як у нас можуть виникати ситуації, коли нам потрібно дізнатись щось задопомогою, якраз цих функцій, а ось одного з прикладу:
    ```Python
    my_list = [1, 2, 3, 4, 5]
    print("Довжина списку:", len(my_list))

    text = "Привіт, світ!"
    print("Довжина рядка:", len(text))
    ```
    1. В завданні четвертому, ми зачіпили досить цікаву тему, як цикли, вони в сучасному програмувані, дуже важливі, але також важливо - це ними добре володіти, так як якщо ми будемо знати, як вони працюють, але неефективно, тоді ми просто будемо витрачати ресурс, для непотрібного циклу, який можна зробити простіше і оптимізованіше, я дізнався, що циклів буває два найважливіших цикла, це for і while, ось приклад одного коду з окремого файлу:
    ```Python
    count = 0
    while count < 5:
    print("Лічильник:", count)
    count += 1
    ```
    1. В п'ятому завдані ми дійшли теж до немало важливої теми, такої, як розгалуження, вони часто використовувались мною в інших мовах програмування, тому для мене це не від'ємні оператори в мовах програмування, ось один приклад з окремого файлу:
    ```Python
    number = 12
    if 10 <= number <= 20:
        if number % 2 == 0:
            print("Число парне і входить у діапазон від 10 до 20")
        else:
            print("Число непарне і входить у діапазон від 10 до 20")
    else:
        print("Число не входить у діапазон від 10 до 20")
    ```
    1. В шостому завданні я дізнався про конструктори, задопомогою яких ми можемо виловлювати помилки, так як в Python код не компілюється а виконується відразу, тому ми можемо використовувати їх для цього, ось приклад:
    ```Python
    # Приклад з обробкою помилок під час конвертації рядка в число
    user_input = "привіт"
    try:
        number = int(user_input)
        print("Ви ввели число:", number)
    except ValueError as e:
        print("Помилка: Невірний формат числа:", e)
    except Exception as e:
        print("Сталася інша помилка:", e)
    finally:
        print("Процес завершено.")
    ```
    1. В сьомому завданні, ми використовували команду with через яку, можна зв'язуватись наприклад до файлу, тобто вносити дані в файл, і звідти витягувати те що нам потрібно, або також використовується для того щоб під'єднувати базиданих або щось подібне, ось приклад коду:
    ```Python
    # Запис у файл з використанням контекст-менеджера
    file_name = "example.txt"

    # Запис даних у файл
    with open(file_name, "w") as f:
        f.write("Це перший рядок.\n")
        f.write("Це другий рядок.\n")
        f.write("І ще один рядок!\n")

    # Читання даних з файлу
    with open(file_name, "r") as f:
        print("Вміст файлу:")
        for line in f:
            print(line.strip())
    ```
    1. В восьмому завданні, ми використовували Лямбди, насправді з ними я не сильно зрозумів, як взаємодіяти, це типу скорочений вигляд функції, тому я попросив в chatGPT, пояснення попросити, а заодно і приклад:
    ```Python
    # Лямбда-функція для обчислення квадрата числа
    square = lambda x: x ** 2

    # Тестування лямбда-функції
    print("Квадрат числа 5:", square(5))
    print("Квадрат числа 10:", square(10)) 

    # Використання лямбда-функції в функції map()
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    print("Квадрати чисел:", squared_numbers) 
    ```
Я виконав наступне завдання, тільки я не бачу сенсу вставляти в звіт все що він мені написав, тому я виділив для цього спеціально файл, де я перекинув, його відповідь в ipynb формат, в якому я використовував, markdown, щоб записати тему і короткий матеріал, а також приклад в вигляді коду, файл називається 'Example_from_ChatGPT.ipynb'.
### Висновок:
🔍 Що зроблено в роботі:
У цій роботі виконано багато цікавих завдань, зокрема детальне вивчення основ Python. Ми розглянули базові принципи програмування цією мовою, що допомагає закласти міцний фундамент для подальшого навчання.

🎯 Чи досягнуто мети роботи:
Так, цілі досягнуті! Все, що було зроблено в рамках цієї роботи, навчало практичному використанню операторів та функцій Python.

📚 Які нові знання отримано:
Я дізнався багато нового, зокрема про вбудовані константи, такі як None, а також про лямбда-функції та конструктори. Це особливості, які є унікальними для Python, що виявилося дуже цікавим, адже раніше я здебільшого працював з C++ та C#.

❔ Чи вдалося відповісти на всі питання, що виникали під час роботи:
Так, на всі питання я знайшов відповіді, або ж безпосередньо в процесі роботи, або за допомогою ChatGPT, що пояснив усе необхідне.

✅ Чи вдалося виконати всі завдання:
Однозначно так!

⚙️ Чи виникли складності у виконанні завдання:
Ні, складнощів не було, адже це були лише приклади, а не якісь складні завдання.

💬 Чи подобається такий формат здачі роботи (Feedback):
Так, дуже! Я вже писав у попередній роботі, що цей формат дійсно зручний та цікавий!

✨ Побажання для покращення (Suggestions):
Було б чудово заглиблюватися у матеріал ще більше. Окрім прикладів, можна було б додати завдання, яке дозволить застосувати нові знання у конкретній задачі.



