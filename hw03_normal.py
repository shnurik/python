
__author__ = 'Корнейчук Александр Николаевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci():
    fib1 = fib2 = 1
    m = int(input("Введите последний ряд: "))
    for i in range(0, m):
        fib1, fib2 = fib2, fib1 + fib2
        print(i + 1, fib2)


print(fibonacci())


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = []
for x in range(-5, 5):
    if x > 0:
        a.append(x)
print(a)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
