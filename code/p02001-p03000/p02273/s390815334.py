import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

sin60 = math.sqrt(3) / 2
cos60 = 1/ 2

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "{:.8f} {:.8f}".format(self.x, self.y)


def koch(n: int, p1, p2):
    if n == 0:
        return
    s = Position((2 * p1.x + p2.x) / 3, (2 * p1.y + p2.y) / 3)
    t = Position((p1.x + 2 * p2.x) / 3, (p1.y +  2 * p2.y) / 3)
    u = Position((t.x - s.x) * cos60 - (t.y - s.y) * sin60 + s.x,
                 (t.x - s.x) * sin60 + (t.y - s.y) * cos60 + s.y)
    koch(n - 1, p1, s)
    print(s)
    koch(n-1, s, u)
    print(u)
    koch(n-1, u, t)
    print(t)
    koch(n-1, t, p2)



def main():
    n = int(input())
    p1 = Position(0.0, 0.0)
    p2 = Position(100.0, 0.0)
    print(p1)
    koch(n, p1, p2)
    print(p2)

if __name__ == '__main__':
    main()

