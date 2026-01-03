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

s = lc()

cnt = Counter([])

for si in s:
    cnt[si] += 1
    

ans = True

for key, value in cnt.items():
    if value != 1:
        ans = False
        break
    
if ans:
    print("yes")
else:
    print("no")