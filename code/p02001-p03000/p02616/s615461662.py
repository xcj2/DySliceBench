import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    Lp=[]
    Lm=[]
    Lz=[]
    for i in range(N):
        if A[i]==0:
            Lz.append(0)
        elif A[i]>0:
            Lp.append(A[i])
        else:
            Lm.append(A[i])
            
    Lp.sort(reverse=True)
    Lm.sort()
    
    Np=len(Lp)
    Nm=len(Lm)
    
    if len(Lp)+len(Lm)<K:#どうしても0が入る
        print(0)
        exit()
    if K==1:
        print(max(A))
        exit()
    if max(A)<=0:#正数がない
        if K%2==0:
            A.sort()
        else:
            A.sort(reverse=True)
        ans=1
        for i in range(K):
            ans=(ans*A[i])%mod
        print(ans)
        exit()
    if K==N:
        ans=1
        for i in range(N):
            ans=(ans*A[i])%mod
        print(ans)
        exit()
    
    Lp.append(0)
    Lp.append(0)
    Lp.append(0)
    Lm.append(0)
    Lm.append(0)
    nowp=0
    nowm=0
    
    ans=1
    if K%2==0:
        for i in range(K//2):
            a=Lp[nowp]*Lp[nowp+1]
            b=Lm[nowm]*Lm[nowm+1]
            if a>=b:
                ans=(ans*a)%mod
                nowp+=2
            else:
                ans=(ans*b)%mod
                nowm+=2
    else:
        ans=Lp[0]
        nowp+=1
        for i in range(K//2):
            a=Lp[nowp]*Lp[nowp+1]
            b=Lm[nowm]*Lm[nowm+1]
            if a>=b:
                ans=(ans*a)%mod
                nowp+=2
            else:
                ans=(ans*b)%mod
                nowm+=2
    print(ans)
        
            

        
 
    
            
            

main()
