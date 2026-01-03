from collections import Counter
from functools import reduce
import bisect
import fractions
import math
import statistics
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]  # LIST INT
def LF(): return [float(x) for x in sys.stdin.readline().split()]  # LIST FLOAT
def LS(): return sys.stdin.readline().split()  # LIST STRING
def MI(): return map(int, sys.stdin.readline().split())  # MAP INT
def II(): return int(sys.stdin.readline())  # INPUT INT
def IS(): return input()  # INPUT STRING
def P(x): return print(x)
def C(x): return Counter(x)
def GCD_LIST(numbers):  # Greatest Common Divisor
    return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers):  # Least Common Multiple
    return reduce(LCM, numbers)
def LCM(m, n):
    return (m * n // fractions.gcd(m, n))


n, a = II(), LI()
counter = sorted(C(a).items(), key=lambda x: x[0], reverse=True)
for i in range(n):
    if 4 <= counter[i][1]:
        print(counter[i][0] ** 2)
        exit()
    elif 2 <= counter[i][1]:
        for j in range(i+1, n):
            if 2 <= counter[j][1]:
                print(counter[i][0] * counter[j][0])
                exit()
print(0)
