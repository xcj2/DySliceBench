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

from itertools import accumulate

n,k = li()
a = list(li())

a_cum = [0] + list(accumulate(a))
sm_lst = []
for i in range(n+1):
    for j in range(i+1,n+1):
        sm_lst.append(a_cum[j] - a_cum[i])
        
pop = sm_lst
ans = 0
for bit in range(40,-1,-1):
    yes=[]
    no=[]
    
    for s in pop:
        if s & (1<<bit):
            yes.append(s)
        else:
            no.append(s)
            
    if len(yes) >= k:
        ans += (1<<bit)
        pop = yes
        

print(ans)
    