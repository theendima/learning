# file_names = ["document.txt", "image1.jpg", "docement2.txt", "imeage2.jpg"] # cписок с именами файлов

# for file_name in file_names: # file_name  меняется каждый раз когда проходит цикл 4 названия 4 цикла
#     print(file_name)


# greeting = "Hello, w0rld!"
# count_o = 0
# for char in greeting:
#     if char == "0":
#         count_o += 1
#         print(char)
# if count_o == 0:
#     print("не найдено")
# print(f" То что мы нашли равно, {count_o}")

# students = ["alice", "bob", "Chralie", "David"]

# for student in students: #  сначала выводится имя из списка/листа / потом развертывение
#     print(student)
#     for char in student:
#         print(char)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for num in numbers:
#     if num %2 == 0:
#         continue # по факту если делится на 2 то есть четное то слово  continue  возвращает нас к циклу и переносит дальше
#     # если не зашло то  число выводится в терминал
#     print(num)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for num in numbers:
#     if num == 10:
#         break # выводится все числа что до были указаны до 10
#     print(num)

# range_object = range(10) 
# print(range_object) # показывает интервал от 0 до введенного нами числа/ примера в данном случае от 0 до 10 (10) не входит
# numbers = list(range_object) # выводит весь список в листе/списке
# print(numbers)

# range_object = range(1,10, 2)  # задает список вывода  в данном случае от 1 до 10 + шаг 2
# numbers = list(range_object) # выводит весь список в листе/списке
# print(numbers)

# range_object = range(10, 1, -1)  # последовательность может быть и убывающей  по типу от 10 до 1 с шагом -1
# numbers = list(range_object) # выводит весь список в листе/списке
# print(numbers)


# # здесь мы наращиваем  +1 в списке
# numbers = [10, 11, 12 ,13, 14, 15, 16, 17]

# # for i in range(len(numbers)): # куждую переменную вытаскивает отдельно 
# #     numbers[i] +=1 # наращиваем по отдельности +1
# # print(numbers)

greeting = "Hello, world!"
indexes = []
count = 0
for i in range(len(greeting)): #ищет в строке
    if greeting[i] == "o": # что ищем
        count += 1 # добавляем +1 если нашло
        indexes.append(i) # показывает на каких позициях нашло
print(count)
print(indexes)
