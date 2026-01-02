#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    A,B,C,D,E,F=MI()
    #dp[i][j]はi*100gのみずにjgの砂糖
    N=F//100+1
    dp=[[0]*(F+1) for _ in range(N)]
    
    dp[0][0]=1
    ansd=0
    ans=[100*A,0]
    
    AB=[A,B]
    CD=[C,D]
    
    for i in range(N):
        if dp[i][0]==1:
            for k in range(2):
                ii=i+AB[k]
                if ii<N:
                    dp[ii][0]=1
        for j in range(F+1):
            if dp[i][j]==1:
                for k in range(2):
                    jj=j+CD[k]
                    if jj<=F and i*100+jj<=F and jj<=E*i:
                        dp[i][jj]=1
                        d=jj/(100*i+jj)
                        if d>ansd:
                            ans=[100*i+jj,jj]
                            ansd=d
    print(' '.join(map(str, ans)))
    

    

main()
