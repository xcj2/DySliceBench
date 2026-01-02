import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    M=10**6+5
    dp=[1]*M
    A.sort()
    L=[A[0]]
    L2=set([])
    for i in range(1,N):
        if A[i]!=L[-1]:
            L.append(A[i])
        else:
            L2.add(A[i])
            
    for i in range(len(L)):
        temp=L[i]
        if dp[temp]==1:
            temp+=L[i]
            while temp<M:
                dp[temp]=0
                temp+=L[i]
        
    ans=0    
    for i in L2:
        dp[i]=0
        
    for i in range(len(L)):
        if dp[L[i]]==1:
            ans+=1
            
            
    

         
            
    print(ans)
                
    
    


main()
