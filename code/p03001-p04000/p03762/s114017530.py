import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    x=LI()
    y=LI()
    dx=[0]*(N-1)
    dy=[0]*(M-1)
    for i in range(N-1):
        dx[i]=x[i+1]-x[i]
    for i in range(M-1):
        dy[i]=y[i+1]-y[i]
    
    NN=max(N,M)+3
    #S[a]は1~aまでの和
    S=[0]*(NN+1)
    for i in range(1,NN+1):
        S[i]+=S[i-1]+i
        
    #端からa番目の要素を何回使う?
    def calc(a,nm):
        if nm%2==1 and a==(nm+1)//2:#aが中央の場合
            return S[a]+S[a-1]
        else:
            return 2*S[a]+(nm-2*a)*a
    

    X=0
    for i in range(N-1):
        X+=calc(i+1,N-1)*dx[i]
        X%=mod
        
    Y=0
    for i in range(M-1):
        Y+=calc(i+1,M-1)*dy[i]
        Y%=mod
        
    print((X*Y)%mod)
    

main()
