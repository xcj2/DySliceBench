import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    L=[0]*N
    
    #売り:1
    for i in range(1,N):
        if A[i]>A[i-1]:
            L[i]=1
            if L[i-1]==1:
                L[i-1]=0
            else:
                L[i-1]=2
                
    mon=1000
    kabu=0
    
    for i in range(N):
        if L[i]==2:
            kabu=mon//A[i]
            mon-=kabu*A[i]
        elif L[i]==1:
            mon+=kabu*A[i]
            kabu=0
            
    print(mon)
                
    

main()
