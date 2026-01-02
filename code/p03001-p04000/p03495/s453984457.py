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

n,k = li()
a = list(li())

cnt = Counter(a)

al = cnt.most_common()

if len(al) <= k:
    print(0)
else:
    ans = 0
    for _, v in al[k:]:
        ans += v
        
    print(ans)