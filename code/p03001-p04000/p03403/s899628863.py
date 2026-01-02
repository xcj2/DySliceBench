from functools import reduce
from decimal import *
from operator import mul

def main():
    n = int(input())
    a = input_list()
    a.insert(0, 0)
    a.append(0)
    total = 0
    for i in range(1, n+2):
        total += abs(a[i] - a[i-1])
    for i in range(1, n+1):
        tobashi = abs(a[i+1] - a[i-1])
        skip = abs(a[i] - a[i-1]) + abs(a[i+1] - a[i])
        print(total - skip + tobashi)

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
