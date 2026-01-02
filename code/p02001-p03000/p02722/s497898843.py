from collections import deque
import sys
sys.setrecursionlimit(200000)
import math


def divisor(n):
    divs = list()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
        i += 1
    return list(sorted(divs))


def read():
    N = int(input())
    return N,


def solve(N):
    ptn = deque()
    factors_n1 = divisor(N-1)[1:]
    factors_n = divisor(N)[1:]
    count = len(factors_n1)
    for k in factors_n:
        n = N
        while n >= k:
            if n % k == 0:
                n = n // k
            else:
                n = n % k
        if n == 1:
            count += 1
    return count
    

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
