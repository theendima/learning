# fruits = ["apple", "banana", "cherry"] #создание списка
# print(fruits[1:3]) # вывод элементов с 1 по 2 (не включая 3)

# my_list =list([1]) # cоздание списка с помощью функции list()
# print(my_list)

# fruits = ["apple", "banana", "cherry"] #создание списка
# print(len(fruits)) # вывод количества элементов в списке

# fruits = ["apple", "banana", "cherry", 1, True, [1, True]] #создание списка c разными типами данных
# print(fruits) # вывод списка

# my_l1 = [1, 2, 3]
# my_l2 = [3, 4, 5]
# my_l3 = [1, 2, 3]
# print(my_l1 == my_l2) # сравнение списков выоводится булевая
# print(my_l1 == my_l3) # сравнение списков

# fruits = ["apple", "banana", "cherry"] #создание списка
# print("banana" in fruits) # проверка наличия элемента в списке выводится булевая
# print("banana" if "banana" in fruits else "нету такого") # проверка наличия элемента в списке и вывод слова "banana" если элемент есть и "нету такого" если элемента нету

# el1 = ["apple"]
# el2 = ["banana"]
# el3 = ["cherry"]
# fruits = el1 + el2 + el3 # объединение списков
# print(fruits) # вывод объединенного списка

# word = "Hello"
# my_l = list(word) # создание списка из строки
# print(my_l) # вывод списка из строки

# fruits = ["apple", "banana", "cherry"]
# fruits.append("Melon") # добавление элемента в конец списка
# fruits.insert(1, "Watermelon") # добавление элемента по индексу
# print(fruits) # вывод списка с добавленным элементом

# my_str = "Hello, world"
# my_str.replace("world", "Dima") # производится замена строки, но так как строки неизменяемый тип данных, то результат замены не сохраняется в переменной my_str
# new_str = my_str.replace("world", "Dima") # сохраняем результат замены в новой переменной
# print(my_str) # вывод строки без изменений, так как строка неизменяемый тип данных
# print(new_str) # вывод строки с заменой, так как результат замены сохранен в новой переменной

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana") # удаление элемента по значению
# print(fruits) # вывод списка с удаленным элементом

# fruits = ["apple", "banana", "cherry"]
# fruits.pop() # удаление элемента по индексу
# print(fruits) # вывод списка с удаленным элементом

# fruits = ["apple", "banana", "cherry"]
# fruit = ["melon", grape] = ["melon", "grape"] # распаковка списка в переменные
# print(fruit) # вывод переменной с распакованным списком

# fruits = ["apple", "banana", "cherry"]
# fruit = ["melon", "grape"] 
# fruits.extend(fruit) # расширение списка другим списком
# print(fruits) # вывод расширенного списка

# fruits = ["apple", "banana", "cherry"]
# fruits.reverse() # разворот списка
# fruit = reversed(fruits) # разворот списка с помощью функции reversed() возвращает итератор
# print(fruits) # вывод развернутого списка
# print(fruit)

# my_string = "Hello, world and Python"
# my_list = my_string.split(" ")
# print(my_list) # вывод списка, созданного из строки с помощью метода split() разделяя строку по пробелу

# my_str = "Hello, world and Python"
# my_l = my_str.split(" ")
# print(my_l)
# joined_string = " ".join(my_l)
# print(joined_string)


my_l = [1, 3, 4564654654, 342134234]
print(max(my_l)) # узнаем какой максимальный эелемент в списке
print(min(my_l)) 
print(sum(my_l)) 

