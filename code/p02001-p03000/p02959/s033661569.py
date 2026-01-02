import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    B=LI()
    
    ans=0
    
    for i in range(N):
        if A[i]>=B[i]:
            ans+=B[i]
        else:
            ans+=A[i]
            rem=B[i] - A[i]
            if A[i+1]>=rem:
                ans+=rem
                A[i+1]-=rem
            else:
                ans+=A[i+1]
                A[i+1]=0
                
                
    print(ans)
            
        

main()
