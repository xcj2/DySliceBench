import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    a=LI()
    L=[]
    S=[0]*(N+1)
    
    for i in range(N):
        S[i+1]=S[i]+a[i]
        
    for i in range(N+1):
        for j in range(i+1,N+1):
            s=S[j]-S[i]
            L.append(s)
            
    x=0
    #答えがxになりうるか
    N2=43
    p=[1]*N2
    for i in range(N2-1):
        p[i+1]=p[i]*2
        
    for i in range(N2):
        temp=x+p[N2-1-i]
        cnt=0
        for a in L:
            if (a&temp)==temp:
                cnt+=1
        if cnt>=K:
            x=temp
            
    print(x)
            

main()
