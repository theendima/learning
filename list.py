# fruit = ["apple", "banana", "cherry"] # обычная запись
# print(fruit) 

# my_list = list((1, 2)) # вариант записи с вызовом list(())
# print(my_list)

# fruit = ["apple", "banana", "cherry"] # обычная запись
# print(len(fruit))  #  выводит количество элементов то есть 3 элемента

# my_list = ["apple", 1, 1.534, True] # можно выводить все что  угодно ну лучше так не делать
# print(my_list)

# l1 = [1, 2, 3]
# l2 = [1, 4, 3]
# l3 = [1, 2, 3]
# print(l1 == l2) #примеры сравнения списков
# print(l1 == l3)

# print(bool([])) # при пустом списке пишет False
# print(bool([0])) # список чем то заполнен значит true
# print(bool([1])) # список чем то заполнен значит true

# fruit = ["apple", "banana", "cherry"]
# print("banana" in fruit)
# print("coke" in fruit) #  припомщи ключевого слова  in  можно проверить есть ли там  этот элемент в  списке

# el1= "apple"
# el2 = "banana"
# el3 = "cherry" 

# fruit = [el1, el2, el3] # создание списка из элементов
# print(fruit)

# word = "hello"
# my_l = list(word) #создание списка из переменных
# print(my_l)

# my_l1 = [1, 2, 3]
# my_l2 = [3, 4, 5]
# my_l3 = my_l1 + my_l2   #слаживание списков
# print(my_l1 + my_l2)
# print(my_l3)

# fruit = ["apple", "banana", "cherry"]
# fruit.append("watemelon") # c использованием методов  :append"  добавляем  новое в список
# print(fruit) # изменения происходят в самом списке

# my_str = "hello, world"
# new_str = my_str.replace("world", "python") # изменение в  новой переменной замены
# print(my_str)
# print(new_str)

# fruits = ["apple", "banana", "cherry"]

# fruit =fruits.pop() #удалил и присвоиз
# print(fruit)
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits2 =["fig", "grape"]

# fruits.extend(fruits2) # добавление списка 1 в другой методом extend
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits.reverse() #реверс списка
# print(fruits)

# my_l = [1, 69, 75, 1.54, 10 ]
# #my_l.sort() # сортировка в списке по возрастанию
# my_l.sort(reverse=True) # сортировка в списке по убыванию
# print(my_l)

# my_str = "My name is Dima"
# my_list =my_str.split(" ") #разделение обычной строчки  в лист  с использованием разделителя  split

# print(my_list)

# join_str = " ".join(my_list) #соединение из списка в  строчку
# print(join_str)

my_l = [1, 69, 75, 1.54, 10 ]
print(max(my_l)) # так узнаем максимальный элемент в списке
print(min(my_l)) # так узнаем минимальный элемент в списке
print(sum(my_l)) # так узнаем сумму элементов