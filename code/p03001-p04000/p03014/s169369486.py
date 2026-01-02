import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    S=[]
    S.append(["#"]*(W+2))
    for i in range(H):
        s=["#"]+list(input())+["#"]
        S.append(s)
    S.append(["#"]*(W+2))
    
    L=[[-1]*(W+2) for _ in range(H+2)]
    R=[[-1]*(W+2) for _ in range(H+2)]
    U=[[-1]*(W+2) for _ in range(H+2)]
    D=[[-1]*(W+2) for _ in range(H+2)]
    
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i][j]!="#":
                L[i][j]=L[i][j-1]+1
                U[i][j]=U[i-1][j]+1
                
    for i in range(H,0,-1):
        for j in range(W,0,-1):
            if S[i][j]!="#":
                R[i][j]=R[i][j+1]+1
                D[i][j]=D[i+1][j]+1
                
    ans=0
    
    for i in range(H+2):
        for j in range(W+2):
            if S[i][j]!="#":
                temp=L[i][j]+R[i][j]+U[i][j]+D[i][j]+1
                ans=max(ans,temp)
                
    # for i in range(H+2):
    #     print(L[i])
    # for i in range(H+2):
    #     print(R[i])
    # for i in range(H+2):
    #     print(U[i])
    # for i in range(H+2):
    #     print(D[i])
                
    print(ans)

main()
