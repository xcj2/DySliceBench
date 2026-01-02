from functools import reduce
from decimal import *
from operator import mul

def main():
    n = int(input())
    p = prime_factorize(n)
    sa = list(sorted(p))
    pp = []
    num = 1
    for i, v in enumerate(sa):
        if i > 0 and sa[i-1] != v:
            num = 1
        num *= v
        if num not in pp and n % num == 0:
            pp.append(num)
            num = 1
    print(len(pp))

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
