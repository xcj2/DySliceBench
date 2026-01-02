import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    c=list(input())
    w=[0]*(N+1)
    r=[0]*(N+1)
    
    for i in range(N):
        if c[i]=="W":
            w[i+1]+=1
        else:
            r[i]+=1
            
    for i in range(N):
        w[i+1]+=w[i]
        
    for i in range(N,0,-1):
        r[i-1]+=r[i]
        
    ans=N
    for i in range(N+1):
        temp=max(w[i],r[i])
        ans=min(ans,temp)
        
    print(ans)

        
            

    

main()
