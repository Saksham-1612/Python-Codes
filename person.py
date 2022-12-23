import datetime


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def check(self):
        today = datetime.date().today()
        age = today.year-self.dob.year
        if today < datetime.date(today.year.self.dob.month, self.dob.dob.day):
            age = 1
        if age >= 18:
            print(self.name, ",congrulations... You are eligible to void")
        else:
            print(self.name, "Sorry....you should be at least 18 year")


p = Person("Saksham", datetime.date(1992, 12, 11))
p.check()
