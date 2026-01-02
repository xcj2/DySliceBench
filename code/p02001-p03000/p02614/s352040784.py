#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b

def main():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(input())

    ans = 0
    for i in product([0, 1], repeat=H):
        for j in product([0, 1], repeat=W):
            black = 0
            for h in range(H):
                for w in range(W):
                    if i[h] == 1 and j[w] == 1 and c[h][w] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
