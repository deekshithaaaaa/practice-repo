try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("This block always executes, whether there was an error or not.")
