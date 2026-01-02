import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)

def main():
    @lru_cache(maxsize=None)
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    def cul(n,x):
        l=len(x)
        b=[x[i] for i in range(l)]
        b.pop(n)
        tmp=b[0]
        for i in range(1,l-1):
            tmp=gcd(tmp,b[i])
        return tmp

    ans=0
    for i in range(p):
        s=cul(i,a[:p])
        if s>ans: ans=s
    print(ans)

if __name__=='__main__':
    N, *a = map(int, sys.stdin.read().split())
    p=50
    if p>N: p=N
    main()