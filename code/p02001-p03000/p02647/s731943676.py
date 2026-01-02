import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    
    mod=10**9+7
    N,K=MI()
    A=LI()
    
    for j in range(K):
        S=[0]*(N+1)
        for i in range(N):
            l=max(0,i-A[i])
            r=min(N-1,i+A[i])
            S[l]+=1
            S[r+1]-=1
            
        temp=0
        for i in range(N):
            temp+=S[i]
            S[i+1]+=S[i]
            A[i]=S[i]
            
        if temp==N*N:
            break
        
    print(' '.join(map(str,A)))
            
        
        

        
    
    
    

main()
