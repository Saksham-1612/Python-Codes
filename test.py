myfile = open(r"C:\Code\Python\File Handling\files\abc.txt", "w+")
myfile.write("hii")
str = myfile.read()
print(str)
