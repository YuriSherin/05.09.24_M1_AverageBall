# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл.

# На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        # множество

students = list(students)       # преобразуем множество в список
students.sort()                 # отсортируем список. По умолчанию сортировка по возрастанию

dict_average_ball = {}          # создадим словарь

index = 0                       # вспомогательная переменная

# Очевидно, что циклы использовать не разрешено. Поэтому повторяем код 5 раз, по количеству студентов в списке

average_ball = sum(grades[index]) / len(grades[index])  # расчет среднего бала для студента
dict_average_ball[students[index]] = average_ball       # добавление нового элемента в словарь
index += 1                                              # увеличим вспомогательную переменную

average_ball = sum(grades[index]) / len(grades[index])
dict_average_ball[students[index]] = average_ball
index += 1

average_ball = sum(grades[index]) / len(grades[index])
dict_average_ball[students[index]] = average_ball
index += 1

average_ball = sum(grades[index]) / len(grades[index])
dict_average_ball[students[index]] = average_ball
index += 1

average_ball = sum(grades[index]) / len(grades[index])
dict_average_ball[students[index]] = average_ball

print(dict_average_ball)    # Вывод словаря в консоль

print('-' * 70)

# =====================================================================
# С использованием циклов задача упрощается
dict_average_ball = {}          # создадим словарь
index = 0                       # вспомогательная переменная

for name_student in students:   # перебор всех элементов списка
    dict_average_ball[name_student] = sum(grades[index]) / len(grades[index])
    index += 1

print(dict_average_ball)        # вывод в консоль