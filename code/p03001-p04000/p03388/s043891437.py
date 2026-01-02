# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    Q=int(input())
    for _ in range(Q):
        a,b=map(int,input().split())
        if a==b:
            print(a+b-2)
            continue
        
        ans=0
        if a<b:
            a,b=b,a
        ans+=b-1
        def nibutan(ok,ng):
            while abs(ok-ng) > 1:
                mid = (ok + ng) // 2
                if solve(mid):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        def solve(mid):
            return mid**2<a*b
        
        sq=nibutan(0,10**9)
        if sq*(sq+1)<a*b:
            p,q=sq,sq+1
        else:
            p,q=sq,sq
        ans+=q-b
        ans+=p-1
        print(ans)
        
                

if __name__ == '__main__':
    main()
