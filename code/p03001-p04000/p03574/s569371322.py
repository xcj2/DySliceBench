#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    S=[[] for _ in range(H+2)]
    S[0]="."*(W+2)
    
    for i in range(H):
        S[i+1]=list("." + input() + ".")
    S[-1]="."*(W+2)
    
    
    dx=[0,0,1,1,1,-1,-1,-1]
    dy=[1,-1,1,0,-1,1,0,-1]
    
    def se(ii,jj):
        cnt=0
        for k in range(8):
            i=ii+dx[k]
            j=jj+dy[k]
            if S[i][j]=="#":
                cnt+=1
        return cnt
    
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i][j]==".":
                S[i][j]=se(i,j)
                
    for i in range(1,H+1):
        print(''.join(map(str, S[i][1:-1])))
            
            
        

main()
