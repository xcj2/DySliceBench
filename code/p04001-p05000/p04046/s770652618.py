from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

H,W,A,B=inpl()
ans = 0

MAX = H+W
fac = [1]*(MAX+1)
for i in range(1,MAX+1):
	fac[i] = (fac[i-1]*i)%mod

gyakugen = [1]*(MAX+1)
gyakugen[MAX] = pow(fac[MAX],mod-2,mod)
for i in range(MAX,0,-1):
	gyakugen[i-1] = (gyakugen[i]*i)%mod

def Comb(n,k):#nCk
	return (fac[n]*gyakugen[k]*gyakugen[n-k])%mod

for x1 in range(B+1,W+1):
	y1 = H-A
	x2 = A
	y2 = W-x1+1
	ans += (Comb(x1+y1-2,y1-1)*Comb(x2+y2-2,y2-1))%mod
	ans %= mod

print(ans)
