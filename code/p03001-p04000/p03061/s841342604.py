import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)

@lru_cache(maxsize=None)
def main():

    def gcd(a,b):
        if b>a:
            a,b=b,a
        while b:
            a,b=b, a%b
        return a

    def cul(n,x):
        l=len(x)
        b=[x[i] for i in range(l)]
        b.pop(n)
        tmp=b[0]
        for i in range(1,l-1):
            tmp=gcd(tmp,b[i])
        return tmp

    N, *a = map(int, sys.stdin.read().split())
    p=50
    if p>N: p=N

    ans=0
    for i in range(p):
        s=cul(i,a[:p])
        if s>ans: ans=s
    print(ans)

if __name__=='__main__':
  main()