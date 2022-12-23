class Circle:
    pi = 3.14159

    def __init__(self, radius):
        print("hell0")

    def display(self):
        area = (self.radius**2)*pi
        circumference = 2*pi*radius
        print("Area - ", area)
        print("Circumference - ", circumference)


c1 = Circle(15)
c1.display()
