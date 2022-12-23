class Human:

    _age = 0
    _gender = "Male"

    def speaks(self):
        print("Hi I am Human")


if __name__ == '__main__':
    Saksham = Human()
    Saksham.age = 15
    print(Saksham._gender)
    Saksham.speaks()
