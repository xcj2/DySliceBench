from functools import reduce
from decimal import *
from operator import mul

def main():
    w, h, k = input_list()
    for x in range(w+1):
        for y in range(h+1):
            if x*(h-y) + y*(w-x) == k:
                print('Yes')
                exit()
    print('No')

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
