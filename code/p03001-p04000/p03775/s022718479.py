import sys
from collections import deque
from itertools import *


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = I()
ans_list = []
divi_list = make_divisors(N)

for i in range(len(divi_list)):
    for q in range(len(divi_list)):
        if divi_list[i] * divi_list[q] == N:
            ans_list.append(
                max(len(str(divi_list[i])), len(str(divi_list[q]))))
print(min(ans_list))
