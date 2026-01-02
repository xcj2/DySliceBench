from fractions import Fraction
import sys
def input():
    return sys.stdin.readline().rstrip('\n')

ZERO = Fraction(0, 1)
Z = 1000000007

class Pow:
    def __init__(self, n):
        self.N = n
        self.e = [1] * (n + 1)
        for i in range(n):
            self.e[i + 1] = (self.e[i] * 2) % Z
    def get(self, n):
        if self.N >= n:
            return self.e[n]
        else:
            for i in range(self.N + 1, n + 1):
                self.e += [(self.e[i] * 2) % Z]
            return self.e[n]


def calc(N, G):
    zz = 0
    r = {}
    r_max = 0
    for a, b in G:
        if b == 0:
            if a == 0:
                zz += 1
            else:
                if 0 in r:
                    r[0][1][1] += 1
                else:
                    r[0] = {1: [0, 1]}
                r_max = max(r_max, r[0][1][1])
        else:
            if a == 0:
                if 0 in r:
                    r[0][1][0] += 1
                else:
                    r[0] = {1: [1, 0]}
                r_max = max(r_max, r[0][1][0])
            else:
                f = Fraction(a, b)
                if f > 0:
                    i = f.numerator
                    j = f.denominator
                    if i in r:
                        if j in r[i]:
                            r[i][j][0] += 1
                        else:
                            r[i][j] = [1, 0]
                    else:
                        r[i] = {j: [1, 0]}
                    r_max = max(r_max, r[i][j][0])
                else:
                    i = f.denominator
                    j = -f.numerator
                    if i in r:
                        if j in r[i]:
                            r[i][j][1] += 1
                        else:
                            r[i][j] = [0, 1]
                    else:
                        r[i] = {j: [0, 1]}
                    r_max = max(r_max, r[i][j][1])
    ans = 1
    pow = Pow(r_max)
    for i in r:
        for j in r[i]:
            ans = (ans * (pow.get(r[i][j][0]) + pow.get(r[i][j][1]) - 1)) % Z
    return (ans + zz - 1) % Z

    

N = int(input())
G = [tuple([int(s) for s in input().split()]) for _ in range(N)]
print(calc(N, G))