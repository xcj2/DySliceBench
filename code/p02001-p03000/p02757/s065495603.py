"""
    Template written to be used by Python Programmers.
    Use at your own risk!!!!
    Owned by enraged(rating - 5 star at CodeChef and Specialist at Codeforces).
"""
import sys
import bisect
import heapq
# from math import *
from collections import defaultdict as dd  # defaultdict(<datatype>) Free of KeyError.
from collections import deque  # deque(list) append(), appendleft(), pop(), popleft() - O(1)
from collections import Counter as c  # Counter(list)  return a dict with {key: count}
from itertools import combinations as comb
from bisect import bisect_left as bl, bisect_right as br, bisect
# sys.setrecursionlimit(2*pow(10, 6))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()


def out(var): sys.stdout.write(var)


def l(): return list(map(int, data().split()))


def sl(): return list(map(str, data().split()))


def sp(): return map(int, data().split())


def ssp(): return map(str, data().split())


def l1d(n, val=0): return [val for i in range(n)]


def l2d(n, m, val=0): return [[val for i in range(n)] for j in range(m)]


n, p = sp()
s = data()
answer = 0
if p == 2:
    for i in range(n):
        if (ord(s[i])-ord('0')) % 2 == 0:
            answer += (i+1)
elif p == 5:
    for i in range(n):
        if int(s[i]) % 5 == 0:
            answer += (i+1)
else:
    dp = dd(int)
    dp[0] += 1
    a, tens = 0, 1
    for i in range(n-1, -1, -1):
        a = (a + int(s[i]) * tens) % p
        answer += dp[a]
        dp[a] += 1
        tens = (tens * 10) % p
out(str(answer))
exit(0)
