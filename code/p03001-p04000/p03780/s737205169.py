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
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=1)
    dp0=[1]*N
    dp1=[1]*N
    mask=(1<<K)-1
    for i in range(N-1):
        if a[i]<K:
            dp0[i+1]=(dp0[i]|(dp0[i]<<a[i]))&mask
        else:
            dp0[i+1]=dp0[i]
        if a[N-i-1]<K:
            dp1[N-i-2]=(dp1[N-i-1]|(dp1[N-i-1]<<a[N-i-1]))&mask
        else:
            dp1[N-i-2]=dp1[N-i-1]
    ans=0
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(i):
        if a[i]<K:
            mask2=((1<<a[i])-1)<<(K-a[i])
            for j in range(dp0[i].bit_length()):
                if j>mask2.bit_length():
                    return True
                if (dp0[i]>>j)&1:
                    if dp1[i]&(mask2>>j):
                        return True
        else:
            return True
        return False
    
    res=nibutan(-1,N)
    print(N-1-res)
    


if __name__ == '__main__':
    main()
