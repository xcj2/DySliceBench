import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

import bisect

def main():
    mod=10**9+7
    N,W=MI()
    w=[0]*N
    w2=[0,0,0,0]#結局4通りしかない
    v2=[[] for _ in range(4)]
    v=[0]*N
    for i in range(N):
        w[i],v[i]=MI()
    w1=w[0]
    for i in range(N):
        w[i]-=w1
        w2[w[i]]+=1
        v2[w[i]].append(v[i])
        
    for i in range(4):
        v2[i].sort(reverse=True)
        
    s=[[0] for _ in range(4)]
    for i in range(4):
        for j in range(len(v2[i])):
            s[i].append(s[i][-1]+v2[i][j])
     
    ans=0       
    for a in range(len(s[0])):
        for b in range(len(s[1])):
            for c in range(len(s[2])):
                for d in range(len(s[3])):
                    ww=b+2*c+3*d+w1*(a+b+c+d)
                    if ww<=W:
                        temp=s[0][a]+s[1][b]+s[2][c]+s[3][d]
                        ans=max(ans,temp)
                        
    print(ans)
                        
        
    

main()
