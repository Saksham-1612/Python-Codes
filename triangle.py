side = input("Enter the side :")
side1 = input("Enter the side :")
side2 = input("Enter the side :")
if(side1 == side2 and side2 == side):
    print("Equilateral triangle found")
elif(side1 == side2 or side2 == side or side == side):
    print("Isoceles trinagle found")
else:
    print("Scalenene")
