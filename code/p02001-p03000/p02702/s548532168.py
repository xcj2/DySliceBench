
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=2019
    S=list(input())
    S=S[::-1]
    N=len(S)
    
    from collections import defaultdict
    dd = defaultdict(int)
    #2019で割ったあまりの個数
    p=[1]*N
    for i in range(N-1):
        p[i+1]=(p[i]*10)%mod
    
    now=0
    dd[0]=1
    for i in range(N):
        now=now+int(S[i])*p[i]
        now%=mod
        dd[now]+=1
        
    ans=0
    for k,v in dd.items():
        ans+=(v*(v-1))//2
    print(ans)
    

main()
