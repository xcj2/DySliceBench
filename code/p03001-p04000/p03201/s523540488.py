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

n = ni()
a = list(li())

from collections import Counter

acnt = Counter(a)

ans = 0
temp = 0
for ai in sorted(a,reverse=True):
    pair = (1<<(ai.bit_length())) - ai
    
    if acnt[ai] > 0 and acnt[pair] > 0:
        if ai == pair:
            temp = (acnt[ai] // 2)
            ans += temp
            acnt[ai] -= (2*temp)
            
        elif ai > pair:
            temp = min(acnt[ai], acnt[pair])
            ans += temp
            acnt[ai] -= temp
            acnt[pair] -= temp
            
print(ans)