#fruits = ["apple", "banana", "cherry", "watermelon"]
#print(fruits[-2]) #вывод списка в 0=1 тип все считается с 0
# fruits[0] = "pineapple" # замена с помощью индекса
# print(fruits)
# fruits[0], fruits[3] = fruits[3], fruits[0] #замена  позици в списке
# print(fruits)

#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
#print(numbers[0:5]) # слайсы срезы выбор  первых 5 элементов из последолвательности
#new_num = numbers[0:5] # выделили в  новую переменную от 1 до 5 позиции (не забывай все считается с 0)
#new_num = numbers[:5] # тоже самое
#print(new_num)
#new_num = numbers[0:len(numbers)] # вывести весь список в срезе
#new_num = numbers[:] # вывести весь список в срезе
#new_num = numbers[:5] # срез
#new_num = numbers[0:10:2] # срез  из списка 0-10  с шагом в 2 типа 0,1,2,3 покажет 0 и2 и так далее
# new_num = numbers[::2] # запись другая но делает тоже что и верхний пример (выборку)

#print(new_num)
#print(numbers[-5:-1]) # использование отрицательных
#print(numbers[::-1]) # реверс списка


# string = "Hello, world"
# print(string[5:]) # вывод с использованием  слайса/среза здесь пример " все выводятся после 5 символа и до конца включительно"


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,] # 3 способа рзвернуть лист
#new_num = numbers[::-1] # 1 spsob
#print(new_num)
#numbers.reverse() # 2 sposob
#print(numbers)
new_numbers = list(reversed(numbers)) # создаем новвую переменную , закидывает ее в   лист и прописываем реверс указывая  основной список

print(type(new_numbers))
print(new_numbers)
