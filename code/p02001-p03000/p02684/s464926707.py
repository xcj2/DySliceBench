import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    
    N2=(K-1).bit_length()+1
    A=[[0]*N for _ in range(N2)]
    A[0]=LI()
    
    for i in range(N):
        A[0][i]-=1
        
    for i in range(N2-1):
        for j in range(N):
            A[i+1][j]=A[i][A[i][j]]
            
    now=0
    for i in range(N2):
        if (K>>i)&1:
            now=A[i][now]
            
    print(now+1)
        
 
    

main()
