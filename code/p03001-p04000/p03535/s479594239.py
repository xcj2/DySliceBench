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

from heapq import heappush, heappop

n = ni()
d = list(li())

def isok(dur: int, d: list):
    pque = [24]
    for di in d:
        heappush(pque, di)

    cur = 0
    while pque:
        tmp = heappop(pque)
        if tmp - cur < dur and tmp >= 12:
            return False
        
        elif tmp - cur < dur:
            heappush(pque, 24-tmp)
            
        else:
            cur = tmp
        
    return True

ans = 13
for cand in range(12, -1, -1):
    if isok(cand, d):
        ans = cand
        break
        
print(ans) 