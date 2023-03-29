from functools import partial

# def power(base, exp):
#     return base ** exp

# square = partial(power, exp=2)
# cube = partial(power, exp=3)

# print(square(5))
# print(cube(5))
# print(cube(base=4))
# print(square(5, exp=4))


# def myfunc(a, b, c):
#     return a, b, c

# a = 10
# f = partial(myfunc, a)
# print(f(20, 30))

# a = 100
# print(f(20, 30))

def outer():
    x = "python"
    a = 0
    def inner():
        nonlocal a
        a += 1
        return f"{a} times"
    return inner

# f = outer()
# print(f())
# del outer
# print(f())
# print(f.__closure__)

f1 = outer()
f2 = outer()
print(f1.__closure__)
print(f2.__closure__)
print(f1())
print(f1())
print(f1())
print(f2())
