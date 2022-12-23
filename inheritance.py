class Person:
    def __init__(self, fname, lname, marks1, marks2, marks3):
        self.fname = fname
        self.lname = lname
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    def printname(self):
        percentage = (self.__marks1+self.__marks2+self.__marks3)/3
        print(self.fname, self.lname, percentage)


class student(Person):
    def __init__(self, fname, lname, year, marks1, marks2, marks3):
        Person.__init__(self, fname, lname, marks1, marks2, marks3)
        super().__init__(fname, lname)
        self.year = year


x = student("mike", "tyson", 2012, 20, 30, 50)
x.printname()
