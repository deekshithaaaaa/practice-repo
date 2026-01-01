try:
    num1 = int(input("enter a number1: "))
    num2 = int(input("enter a number1: "))
    num3  = num1/num2
except ZeroDivisionError:
    print("number cannot be divided by zero")
   