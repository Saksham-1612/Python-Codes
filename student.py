class student:
    def __init__(self, name, rollno, marks1, marks2, marks3):
        self.name = name
        self.rollno = rollno
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    def display(self):
        percentage = ((self.__marks1+self.__marks2+self.__marks3)/3)
        print(self.name, self.rollno, percentage, "%")


s = student("Saksham", 35, 40, 50, 10)
s.display()
print(s._student__marks1)
