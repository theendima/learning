#data = input("введи букавки: ")
#file = open("text.txt", "a")

#file.write("123\n")
#file.write("!!!")
#file.write(data +"\n")
#file.close()
file = open("text.txt", "r")

print(file.read(5))

file.close()
