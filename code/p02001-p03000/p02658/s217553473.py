#import numpy
import math
import sys

def main():
    n = int(input())
    a = sorted(input_list())
    max_n = 10 ** 18
    ans = 1
    for v in a:
        ans *= v
        if ans > max_n:
            ans = -1
            break
        if ans == 0:
            break
    print(ans)


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
    return list(map(int, sys.stdin.readline().split()))


if __name__ == '__main__':
    main()
