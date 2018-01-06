from functools import reduce


def fn(x, y):
    return x * 10 + y


def str2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(lambda x, y: x * 10 + y, map(str2num, '13579')))


def normalize(name):
    return "%s" % (name.capitalize())


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
