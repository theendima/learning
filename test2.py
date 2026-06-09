try:
     x = 5 / 1
     x = int(input())
except ZeroDivisionError:
     print("Нельзя делить на ZERO")
except ValueError:
     print("Ты ввел что то не так")
else:
     print("else")
finally: 
     print("finally") # 