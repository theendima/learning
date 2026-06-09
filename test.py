#try: #обработчик исключений
#    x = int(input("Введите число:"))
#    x += 5
#    print(x)
#except ValueError: 
#    print("Напиши букавки!")


x = 0
while x == 0:
    try: #обработчик исключений
        x = int(input("Введите число:"))
        x += 5
        print(x)
    except ValueError: 
        print("Напиши букавки!")
