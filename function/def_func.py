import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# return tulpe
print(move(100, 100, 60, math.pi / 6))

# TypeError: bad operand type:
# my_abs('123')

# 返回一元二次方程
import math


def quadratic(a, b, c):
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError('bad poerand type', i)
    m = b * b - 4 * a * c
    if m < 0:
        return '此方程无解！'
    elif m == 0:
        x1 = x2 = -b / 2 * a
        print('此方程有2个相同的实根')
    else:
        x1 = (-b + math.sqrt(m)) / 2 * a
        x2 = (-b - math.sqrt(m)) / 2 * a
        print('此方程有2个相同的实根')
    return x1, x2

#参数a,b,c自由入力
print('求解一元二次方程:ax²+bx+c=0')
a=float(input('请输入参数a='))
b=float(input('请输入参数b='))
c=float(input('请输入参数c='))
print('(%sx²+%sx+%s)的解⇒'%(a,b,c),quadratic(a,b,c))
print('漂亮的分割线------------------------------------')
#固定参数的test
print('(%sx²+%sx+%s)的解⇒'%(1,1,1),quadratic(1,1,1)) # '无解！'
print('(%sx²+%sx+%s)的解⇒'%(1,4,4),quadratic(1,4,4)) # '有2个相同的实根:'
print('(%sx²+%sx+%s)的解⇒'%(2,3,1),quadratic(2,3,1)) # '有2个不同的实根:'
print('(%sx²+%sx+%s)的解⇒'%(1,3,-4),quadratic(1,3,-4)) # '有2个不同的实根:'
