import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,X,M=MI()
    use=[0]*M
    loopF=0
    loopN=0
    loopS=0
    loopL=[]
    ans=0
    cnt=0
    
    now=X
    
    if N<=4*M:
        for i in range(N):
            ans+=now
            now=(now**2)%M
        print(ans)
        exit()
            
    
    for i in range(M*3):
        use[now]+=1
        if use[now]==2:
            loopF=1
        if use[now]==3:
            cnt=i
            break
        
        ans+=now
        if loopF:
            loopL.append(now)
            loopN+=1
            loopS+=now
        
        now=(now**2)%M
        
    N2=N-cnt
    loop=N2//loopN
    rem=N2%loopN
    
    ans+=loop*loopS
    ans+=sum(loopL[:rem])
    
    print(ans)
    

main()
