try:
    x = 5 / 1
    x = int(input())
except ZeroDivisionError:
    print("Деление на ноль Невозможно!")
except ValueError:
    print("ВВедите цифру")
else:
    print(" и что")
finally:
    print("Я сделаль!")