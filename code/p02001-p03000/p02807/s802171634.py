import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    x=LI()
    
    #区間を固定して考える．i番目の区間に対して，i番目のスライムが通過する確率は1
    #i-1番目のスライムの確率は1/2，i-2番目のスライムは1/3...
    
    diff=[0]*(N-1)
    for i in range(N-1):
        diff[i]=x[i+1]-x[i]
    
    p1=[1]*N
    for i in range(N-1):
        p1[i+1]=(p1[i]*(i+1))%mod#1から順にNまでかける
        
    a=[0]*N
    for i in range(N):
        #　a[i]は　mod下での　1/(i+1)
        a[i]=pow(i+1,mod-2,mod)
        
        
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=(S[i]+a[i])%mod
        
    ans=0
    for i in range(N-1):
        ans=(ans+S[i+1]*diff[i]*p1[-1])%mod
        
    print(ans)
    
    
    
    

main()
