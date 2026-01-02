import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,K=MI()
    A=LI()
    B=LI()
    AS=[0]*(N+1)
    BS=[0]*(M+1)
    
    for i in range(N):
        AS[i+1]=AS[i]+A[i]
        
    for i in range(M):
        BS[i+1]=BS[i]+B[i]

    import bisect
    
    ans=0
    for i in range(N+1):
        at=AS[i]
        bt=K-at
        if bt<0:
            break
        j=bisect.bisect_right(BS,bt)-1
        temp=i+j
        ans=max(ans,temp)
        
    print(ans)
        

            

main()
