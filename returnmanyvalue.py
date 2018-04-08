import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny, angle


print('%s, %s, %s' % (move(100, 100, 60, math.pi / 6)))
