# fr = ["apple", "banana", "cherry","gpappe"]

# # fr[0] = "z" # подмена 1 элемента
# fr[0], fr[2] = fr[2], fr[0]
# print(fr) 

# sl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 456]
# print(sl[1::])
# print(sl[:2:])
# print(sl[::3])
# print(sl[::-1]) # разворот строк (реверс)

# st = "Heelo, world!"

# #st1 = st.replace("world", "python") #замена


# print(st[5::])

sl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 456] 
sl2 = sl[::-1] # реверс при помощи слайса
sl3 = list(reversed(sl)) # 3 типа развернуть
sl.reverse() # реверс при помощи функции

print(sl)
print(sl2)
print(sl3)