# f = ["apple", "banana", "cheery", "melon"]
# print(f[0]) # вывод по индексу

# f = ["apple", "banana", "cheery", "melon"]
# f[0] = "pinta" # замена в списке

# f = ["apple", "banana", "cheery", "melon"]
# f[0], f[2] = f[2],f[0]
# print(f)

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(n[0:5]) # выборка 5 элементов аналог print(n[:5])
# print(n[2:6]) # выборка по диапозону
# print(n[1:10:2]) # выборка c подиапозону с шагом два аналог print(n[::2])
# print(n[0:len(n)]) # вывод всего списка # print(n[:])

# my_str = "Hello, my dear frind Python"
# print(my_str[5:]) # вывод все что болье 5 буквы

# способа развернуть лист
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nn = list(reversed(n)) # 3 способ
new_n = n[::-1] # 1 способ сделать реверс
n.reverse() #2 способ сделать реверс

print(n)
print(new_n)
print(new_nn)