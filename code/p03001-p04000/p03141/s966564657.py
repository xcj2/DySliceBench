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
ab = [tuple(li()) for _ in range(n)]

que = []
for ai, bi in ab:
    heappush(que, [-ai-bi, ai, bi])
    
cnt = 0
tak = 0
aok = 0
while que:
    sm, ai, bi = heappop(que)
    if cnt % 2 == 0:
        tak += ai
    else:
        aok += bi
        
    cnt += 1
        
print(tak-aok)