import math
import collections

def main():
    x, y = input_list()
    if x < 2 or y < 2:
        print(abs(x-2) * abs(y-2))
    else:
        print((x-2) * (y-2))


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
    return list(map(int, input().split()))


if __name__ == '__main__':
    main()
