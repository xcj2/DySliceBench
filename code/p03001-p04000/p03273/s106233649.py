from functools import reduce
from decimal import *
from operator import mul

def main():
    h, w = input_list()
    masu = []
    for _ in range(h):
        line = list(input())
        masu.append(line)
    rows = [False] * h
    cols = [False] * w
    for i, m in enumerate(masu):
        for j, v in enumerate(m):
            if v == "#":
                rows[i] = True
                cols[j] = True
    for i, m in enumerate(masu):
        if rows[i] is False:
            continue
        a = ''
        for j, v in enumerate(m):
            if cols[j] is False:
                continue
            a += v
        print(a)

def count_tento(l, cur):
    count = 0
    for v in l:
        if v > cur:
            count += 1
    return count

def input_list():
    return list(map(int, input().split()))

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == '__main__':
    main()
