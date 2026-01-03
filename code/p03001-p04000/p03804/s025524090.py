import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    A=[]
    B=[]
    
    for i in range(N):
        A.append(input())
        
    for i in range(M):
        B.append(input())
       
       
        
    def ch(a,b):
        for i in range(M):
            for j in range(M):
                if A[a+i][b+j]!=B[i][j]:
                    return False
        return True
    
     
    f=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if ch(i,j):
                f=1
                break
                
    if f==1:
        print("Yes")
    else:
        print("No")
            

main()
