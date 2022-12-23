classes_held = eval((input("enter your classes_held ")))
classes_taken = eval((input("enter your classes_taken ")))
percentage = (classes_taken/classes_held)*100
print(percentage)
if(percentage < 75):
    print("Not allowed")
else:
    print("allowed")
