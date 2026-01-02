import sys
sys.setrecursionlimit(10**5)

def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LI_(): return [-1*int(x) for x in input().split()]
def II(): return int(input())
def IF(): return float(input())
def LM(func,n): return [[func(x) for x in input().split()]for i in range(n)]
mod = 1000000007
inf = float('INF')


def solve(L):
   L = L[1:-1]
   if L[0] != '[':
       return int(L)//2+1
   ret = []
   s=0
   c = 0

   for i in range(len(L)):
       if L[i] == '[':
           c += 1
       elif L[i] == ']':
           c -= 1
       if c == 0:
           ret.append(solve(L[s:i + 1]))
           s = i + 1
   ret.sort()
   return sum(ret[0:len(ret)//2+1])


N = II()
for i in range(N):
    L = input()
    print(solve(L))


