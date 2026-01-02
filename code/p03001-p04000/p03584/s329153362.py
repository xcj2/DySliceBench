import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=[0]*N
    B=[0]*N
    for i in range(N):
        a,b=MI()
        A[i]=a
        B[i]=b
        
    """
    xorだと思っていたので馬鹿みたいにむずかった...
    
    最大値の最大値，的な．
    Kを二進数表記して，bitが立っている桁を選び，i桁目とする．
    iよりも高位側はKと同じで，
    低位側を全部1にした数K2を考える．
    orがK2を超えなければOk
    """
    
    ans=0
    M=len(bin(K))-2
    
    for i in range(M):
        temp=0
        if K>>i & 1:
            K2=K-(1<<i)
            K2=K2 | ((1<<i)-1)
                    
            for k in range(N):#k番目の数を使うかどうか
                if K2 | A[k] == K2:
                    temp+=B[k]  
            ans=max(ans,temp)
           
    temp=0 
    for k in range(N):#k番目の数を使うかどうか
        if K | A[k] == K:
            temp+=B[k]
    ans=max(ans,temp)
    
    print(ans)
                    
                    
            
        
    
    

main()
