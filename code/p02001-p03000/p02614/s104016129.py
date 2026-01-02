import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,K=MI()
    C=[]
    for i in range(H):
        c=input()
        C.append(c)
    
    import itertools
    ans=0
    for ite in itertools.product([0,1], repeat=H+W):
        temp=0
        for i in range(H):
            for j in range(W):
                if ite[i]==1 or ite[j+H]==1:
                    pass
                else:
                    if C[i][j]=="#":
                        temp+=1
        if temp==K:
            ans+=1
            
    print(ans)

main()
