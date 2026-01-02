import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

import re

n = ni()
s = ns()
cnt = 0
cand = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            stri = str(i)
            strj = str(j)
            strk = str(k)
            first = False
            second = False
            for si in s:
                if si == strk and first and second:
                    cnt += 1
                    break
                elif si == strj and first:
                    second = True
                elif si == stri:
                    first = True

print(cnt)
