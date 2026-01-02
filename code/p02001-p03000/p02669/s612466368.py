import sys
input=sys.stdin.readline
from functools import lru_cache

def solve(n,a,b,c,d):
    @lru_cache(None)
    def f(n):
        if n==0:
            return 0
        if n==1:
            return d
        ans=d*n
        q,r=divmod(n,2)
        if r==0:
            ans=min(ans,f(q)+a)
        else:
            ans=min(ans,f(q)+a+d,f(q+1)+a+d)
        q,r=divmod(n,3)
        if r==0:
            ans=min(ans,f(q)+b)
        elif r==1:
            ans=min(ans,f(q)+b+d)
        else:
            ans=min(ans,f(q+1)+b+d)
        q,r=divmod(n,5)
        if r==0:
            ans=min(ans,f(q)+c)
        elif r==1:
            ans=min(ans,f(q)+c+d)
        elif r==2:
            ans=min(ans,f(q)+c+d*2)
        elif r==3:
            ans=min(ans,f(q+1)+c+d*2)
        else:
            ans=min(ans,f(q+1)+c+d)
        return ans
    return f(n)

def main():
    t=int(input())
    for _ in range(t):
        n,a,b,c,d=map(int,input().split())
        print(solve(n,a,b,c,d))

if __name__=='__main__':
    main()