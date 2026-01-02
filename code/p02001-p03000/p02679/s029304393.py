import sys
from collections import namedtuple, defaultdict
from math import gcd
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        g = gcd(abs(x), abs(y))

        x //= g
        y //= g

        if x < 0:
            x *= -1
            y *= -1

        elif x == 0 and y < 0:
            y *= -1

        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'

def main():
    n = int(input())
    
    p = []
    d = defaultdict(lambda: 0)
    zeros = 0

    for _ in range(n):
        x, y = map(int, input().split())

        if x == 0 and y == 0:
            n -= 1
            zeros += 1
            continue

        p.append(Point(x, y))
        d[p[-1]] += 1

    MOD = 10 ** 9 + 7

    pw = [ pow(2, i, MOD) for i in range(n + 1) ]

    ans = 1
    tot = 0

    for x in d.keys():
        if x.x > 0 and x.y >= 0 and Point(-x.y, x.x) in d:
            s = d[x]
            t = d[Point(-x.y, x.x)]

            tot += s + t
            value = (pw[s] + pw[t] - 1 + MOD) % MOD
            ans = ans * value % MOD

    ans = ans * pw[n - tot] % MOD
    ans = (ans - 1 + MOD + zeros) % MOD

    print(ans)
main()
