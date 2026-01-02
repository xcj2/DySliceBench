#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    ans=[-1]*N
    f=1
    for i in range(M):
        s,c=MI()
        s-=1
        if ans[s]==-1:
            ans[s]=c
        else:
            if ans[s]==c:
               continue
            else:
                f=0
    if ans[0]==0 and N!=1:
        f=0      
      
    if f==0:
        print(-1)
    elif N==1 and (ans[0]==0 or ans[0]==-1):
        print("0")
        
    else:
        for i in range(N):
            if ans[i]==-1:
                ans[i]=0
                if i==0:
                    ans[i]=1
            
        print(''.join(map(str, ans)))

main()
