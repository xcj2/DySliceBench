import math
from decimal import *

def main():
    a, b = input_list()
    print(int(a*b))

def yogen(a, b, angle):
    coss = math.cos((angle/180)*math.pi)
    return math.sqrt(a**2 + b**2 - 2*a*b*coss)


def get_angle(hour, minute):
    h = (hour * 360) / 12 + (minute * 360) / (12 * 60)
    m = (minute * 360) / 60
    angle = abs(h-m)
    return min(angle, 360-angle)

def has(v, l):
    for vl in l:
        if v == vl:
            return True
    return False

def input_list():
    return list(map(Decimal, input().split()))


if __name__ == '__main__':
    main()
