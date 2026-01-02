import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter
from itertools import accumulate

n,m = li()
a = list(li())

acum = list(accumulate(a))
acum = [acumi%m for acumi in acum]

cnt = Counter(acum)

ans = cnt[0]
for k,v in cnt.items():
    ans += v*(v-1)//2
    
print(ans)