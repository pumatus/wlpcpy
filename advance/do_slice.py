# -*- coding: utf-8 -*-

L = ['Michel', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])

print('L[:3] =', L[:3])

print('L[1:3] =', L[1:3])

print('L[-2:] = ', L[-2:])

R = list(range(100))

print('R[:10] =', R[:10])

print('R[-10:] =', R[-10:])

print('R[10:20] =', R[10:20])

print('R[:10:2] =', R[:10:2])

print('R[::5] =', R[::5])


# 迭代 Iteration (字符串也是可迭代对象)
for cd in 'ABC':
    print(cd)

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

# 判断一个对象是否能被迭代, 通过collections模块的iterable类型
from collections import Iterable, Iterator
    # print('',isinstance('adv', Iterable))


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))