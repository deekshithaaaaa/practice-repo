num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
num3 = int(input("enter a num3: "))
num4 = int(input("enter a num4: "))
num5 = int(input("enter a num5: "))
lst = [num1,num2,num3,num4,num5]
largest = max(lst)
print(largest)

for index,i in enumerate(lst):
    print(index,i)
print("even") if largest%2==0 else print("odd")

