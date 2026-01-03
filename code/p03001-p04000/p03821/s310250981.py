import numpy as np
import math
import collections
import fractions
import itertools

def iput(): return int(input())
def mput(): return map(int, input().split())
def lput(): return list(map(int, input().split()))

def solve():
    n = int(input())
    cost = 0
    a, b = [0]*n, [0]*n
    for i in range(n):
        a[i], b[i] = mput()
    inc = 0
    for i in range(n-1, -1, -1):
        a[i] += inc
        mult = math.ceil(a[i]/b[i])*b[i]
        cost += mult - a[i]
        inc += mult - a[i]
    print(cost)
    return 0

if __name__ == "__main__":
    solve()
