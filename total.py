# -*- coding: utf-8 -*-



age = 20
if age <= 18:
    print('your age is', age)
else:
    print('your age is', age - 5)

print(list(range(5)))

# 0 -- 100 相加
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环 条件满足不断循环 条件不满足退出循环 100以内奇数之和

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

abs(100)

# hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 2000


def int2str(self):
    return hex(self)


print('n1 十六进制字符串为: %s\nn2 十六进制字符串为: %s' % (int2str(n1), int2str(n2)))


# 定义函数  求绝对值函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return None


print('绝对值是: %s' % (my_abs(-5)))


# 定义一个空函数  pass 占位符
def nop():
    pass

# 使用内置函数对参数类型做检查
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print('canshu %s' % (my_abs1('1')))

