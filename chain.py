num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
if(num1 == num2):
    print(num1, "is equal to", num2)
elif(num2 == num3):
    print(num2, "is equal to", num3)
elif(num1 == num3):
    print(num1, "is equal to", num3)
elif(num1 > num2):
    if(num1 > num3):
        print(num1)
elif(num2 > num3):
    if(num2 > num1):
        print(num2)
else:
    print(num3)
