class student:

    def __init__(self, n, r, m1, m2, m3):
        self.name = n
        self.__roll_no = r  # private member
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display(self):
        total_marks = self.marks1+self.marks2+self.marks3
        print("Name", self.name)
        print("Roll Number ", self.__roll_no)
        print("marks", total_marks)

    def __del__(self):
        print("Destuctor called")
        self.name


# object
s1 = student("Saksham", 12111097, 15, 16, 18)
print(s1._student__roll_no)  # calling a private member
s1.display()
