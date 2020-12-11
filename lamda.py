def x(a): return a + 10


print(x(5))


def x1(a, b): return a*b


print(x1(5, 6))


def x2(a, b, c): return a+b+c


print(x2(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
