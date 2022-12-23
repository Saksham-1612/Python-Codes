class Employee:
    hike = 1.5
    nEmployee = 0
    # constuctor

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.nEmployee += 1

    def increase(self):
        self.salary = self.salary*Employee.hike

    @classmethod
    def change(cls, amount):
        cls.hike = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


class Programmer(Employee):
    def __init__(self, fname, lname, salary, prog_lang, exp):
        super().__init__(fname, lname, salary)
        self.prog_lang = prog_lang
        self.exp = exp


# print(Employee.nEmployee)
Saksham = Employee("Saksham", "Srivastava", 100000)
Abhishek = Employee.from_str("Abishek-Kumar-760000")
Sak = Programmer("Sak", "sri", 500000, "Ruby", 15)
# print(Employee.nEmployee)
# Rohan = Employee("Rohan", "Yadav", 50000)
# print(Employee.nEmployee)
print(Sak.fname, Sak.lname, Sak.salary, Sak.exp, Sak.prog_lang)
print(Abhishek.fname, Abhishek.lname, Abhishek.salary)
print(Saksham.fname, Saksham.lname, Saksham.salary)
# print(Rohan.fname, Rohan.lname, Rohan.salary)
Employee.change(2)
Saksham.increase()
print(Saksham.salary)
