"""
    Template written to be used by Python Programmers.
    Use at your own risk!!!!
    Owned by enraged(rating - 5 star at CodeChef and Specialist at Codeforces).
"""
import sys
from functools import lru_cache
from collections import defaultdict as dd
def data(): return sys.stdin.readline().strip()
def out(var): sys.stdout.write(str(var))
def outln(var): sys.stdout.write(str(var)+"\n")
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


n, x, y = sp()
dp = dd(int)
for i in range(1, n):
    for j in range(i+1, n+1):
        answer = min(abs(j-i), abs(x-i)+1+abs(j-y), abs(y-i)+1+abs(j-x))
        dp[answer] += 1
for i in range(1, n):
    outln(dp[i])