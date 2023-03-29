from copy import copy, deepcopy


# a = [[1, 2, 3], 'b', 'c']
# b = a.copy()
# c = copy(a)
# d = deepcopy(a)
# print(a is b, a[0] is b[0])
# print(a is c, a[0] is c[0])
# print(a is d, a[0] is d[0])


# x = [[1, 2, 3], [True, False, True], ['a', 'b', 'c']]
# y = list(x)
# # z = copy(x)
# # t = x.copy()
# print(x, y, sep="\n")
# print("\n")
# x.append(['new list'])
# x[1][1] = True
# print(x, y, sep="\n")

# a = [['a', 'b', 'c'], 2, 3]
# b = list(a)
# print(a, b)
# a[0][1] = 'd'
# print(a, b)

# def func(a, *args, b=10, **kwargs):
#     return a + b + sum(args) + sum(kwargs.values())

# print(func(20, 2, 3, 4, b=50, x=100, y = 1000))
# def function(a, b, /, c, d, *, e, f):
#     print (a, b, c, d, e, f)

# print(function(1, 2, 3, d=4, e=5, f=6))
# print(function(1, 2, 3, d=4, e=5, f=6))
