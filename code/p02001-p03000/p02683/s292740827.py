import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    import itertools
    
    N,M,X=MI()
    C=[0]*N
    A=[]
    for i in range(N):
        ca=LI()
        C[i]=ca[0]
        A.append(ca[1:])
        
    ans=10**10
    for ite in itertools.product([0,1], repeat=N):
        score=[0]*M
        temp=0
        for i in range(N):
            if ite[i]:
                temp+=C[i]
                for j in range(M):
                    score[j]+=A[i][j]
        if min(score)>=X:
            ans=min(ans,temp)
            
    if ans==10**10:
        ans=-1
    print(ans)
                
            
       

main()
