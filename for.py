#Цикл for в Python используется для перебора элементов: списков, строк, словарей, диапазонов чисел и других коллекций.

# for i in [1, 2, 3, 4, 5, 6]: # Переменная i по очереди принимает значения из списка.
#     print(i)

# name = "Dima"
# for i in name: # перебор строки
#     print(i) #Цикл проходит по каждому символу строки.

#range() Чаще всего for используется вместе с range().
# for i in range(5): #⚠️ Верхняя граница не включается.
#     print(i)

# for i in range(2,7): # вывод от 2 до 6
#     print(i)

# for i in range(0,11,2): # выводит от 0 до 10 с шагом 2
#     print(i)

# total = 0
# for i in range(1, 6):
#     total += i

# print(total)

# #vСумма чисел Что происходит:
# # 0 + 1 = 1
# # 1 + 2 = 3
# # 3 + 3 = 6
# # 6 + 4 = 10
# # 10 + 5 = 15

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits: #Перебор списка
#     print(fruit)

# fruits = ["apple", "banana", "cherry"] #Получение индекса через enumerate()
# for index, fruits in enumerate(fruits):
#     print(index, fruits)

# for i in range(1,5): #break — остановить цикл.Когда i стало равно 5, цикл завершился.
#     if i == 5:
#         break
#     print(i)

# for i in range(5): #continue — пропустить итерацию Число 2 было пропущено.
#     if i == 2:
#         continue
#     print(i)

# for i in range(3): #Вложенные циклы
#     for j in range(2):
#         print(i, j)

# for i in range(1, 11): #    Практический пример Допустим, нужно вывести только чётные числа:
#     if i % 2 == 0:
#         print(i)