# 利用递归函数计算阶乘
# N！ = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(100) =', fact(998))


# 尾递归
def tail_fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(5, 1))


# 利用递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

        # move(4, 'A', 'B', 'C')
        # print('-------------')


print(move(4, 'A', 'B', 'C'))
