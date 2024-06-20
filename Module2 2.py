# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

# Принимаем 3 числа
first, second, third = input("Введите 3 числа подряд без пробелов: ")

if first == second and first == third: # проверяем равенство всех чисел
    print(3)
elif first == second or first == third or second == third: # проверяем равенство любых двух чисел
    print(2)
else:
    print(0) # выводим 0, если равных чисел нет