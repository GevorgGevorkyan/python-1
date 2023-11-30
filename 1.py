import math

print('1. Сложить 2 числа')
print('2. Вычесть первое из второго')
print('3. Перемножить два числа')
print('4. Разделить первое на второе')
print('5. Возвести в степень N первое число')
print('6. Найти квадратный корень из числа')
print('7. Найти факториал из числа')
print('8. Найти синус')
print('9. Найти косинус')
print('10. Найти тангенс')
print('Введите операцию, которую хотите использовать')

def input_number(prompt):
    while True:
        try:
            print(prompt)
            number = float(input())
            return number
        except ValueError:
            print('Ошибка ввода. Попробуйте ввести числа.')

def calculate_factorial():
    while True:
        try:
            number = int(input_number('Введите число: '))
            if number < 0:
                raise ValueError('Число должно быть положительным')
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(factorial)
            break
        except ValueError:
            print('Ошибка ввода. Попробуйте ввести числа.')

operation = input("")
if operation == "1":
    first_number = input_number('Введите первое число')
    second_number = input_number('Введите второе число')
    print('Сложение чисел:', first_number + second_number)
elif operation == "2":
    first_number = input_number('Введите первое число')
    second_number = input_number('Введите второе число')
    print('Вычитание второго числа из первого:', first_number - second_number)
elif operation == "3":
    first_number = input_number('Введите первое число')
    second_number = input_number('Введите второе число')
    print('Умножение чисел:', first_number * second_number)
elif operation == "4":
    first_number = input_number('Введите первое число')
    second_number = input_number('Введите второе число')
    if second_number == 0:
        print('Вы делите на 0, а так нельзя. Попробуйте другое число.')
    else:
        print('Деление первого на второе:', first_number / second_number)
elif operation == "5":
    base = input_number('Введите число')
    exponent = input_number('Введите степень, в которую хотите возвести')
    print(f'Возведение в степень: {base ** exponent}')
elif operation == "6":
    number = input_number('Введите число')
    print('Квадратный корень из числа:', math.sqrt(number))
elif operation == "7":
    calculate_factorial()
elif operation == "8":
    angle = input_number('Введите угол')
    print('Синус угла:', math.sin(angle))
elif operation == "9":
    angle = input_number('Введите угол')
    print('Косинус угла:', math.cos(angle))
elif operation == "10":
    angle = input_number('Введите угол')
    print('Тангенс угла:', math.tan(angle))