import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


d, n = map(int, input().split())


def func(x):
    cnt = 0
    while x % 100 == 0:
        cnt += 1
        x /= 100
    return cnt == d


cntcnt = 0

for i in range(1, 10000000):
    if func(i):
        cntcnt += 1
        if cntcnt == n:
            print(i)
            exit()
