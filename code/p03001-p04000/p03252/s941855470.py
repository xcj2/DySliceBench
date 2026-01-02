import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

s = ns()
t = ns()

cnt_s = Counter(s)
cnt_t = Counter(t)

val_s = sorted(list(cnt_s.values()))
val_t = sorted(list(cnt_t.values()))

if val_s == val_t:
    print("Yes")
else:
    print("No")