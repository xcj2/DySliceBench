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


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
a = readints()


def func(l):
    if len(l) == n:
        for i in range(len(l)):
            if l[i] % 2 == 0:
                return 1

        return 0
    return func(l+[(a[len(l)])])+func(l+[(a[len(l)]-1)])+func(l+[(a[len(l)]+1)])


print(func([]))
