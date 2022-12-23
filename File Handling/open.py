myfile = open(r"C:\Code\Python\File Handling\files\abc.txt", "a")
# print(myfile.readline(5))
for i in range(3):
    name = input("What is your name : ")
    myfile.write(name)
    myfile.write("\n")

myfile.close()
myfile = open(r"C:\Code\Python\File Handling\files\abc.txt", "r")
print(myfile.read())
myfile.close()
myfile = open(r"C:\Code\Python\File Handling\files\abc.txt", "w")
myfile.flush()
myfile.close()
