class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Person("John", "Doe")
x.printname()
y = Student("Mike", "Olsen")
y.printname()

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Student1(Person):
    def __init__(self, first, lname):
        Person.__init__(self, fname, lname)

# Use the super() Function


class Person4:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname3(self):
        print(self.firstname, self.lastname)


class Student4(Person4):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
