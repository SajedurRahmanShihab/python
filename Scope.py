def myfunc():
    x = 300
    print(x)


myfunc()


def myfunc1():
    x = 300

    def myinnnerfunc():
        print(x)
    myinnnerfunc()


myfunc()

# Global Keyword


def myfunc3():
    global x
    x = 300


myfunc3()
print(x)
