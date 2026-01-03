import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    T=LI()
    A=LI()
    inf=10**9+1
    M1=[inf]*N
    M2=[inf]*N
    m1=[1]*N
    m2=[1]*N
    
    now=1
    for i in range(N):
        t=T[i]
        if t>now:
            m1[i]=t
            M1[i]=t
            now=t
        else:
            M1[i]=now
            
    now=1
    for i in range(N-1,-1,-1):
        t=A[i]
        if t>now:
            m2[i]=t
            M2[i]=t
            now=t
        else:
            M2[i]=now
            
    ans=1
    for i in range(N):
        M=min(M1[i],M2[i])
        m=max(m1[i],m2[i])
        if m>M:
            ans=0
            break
        else:
            ans=(ans*(M-m+1))%mod
            
    print(ans)
        
    
main()
