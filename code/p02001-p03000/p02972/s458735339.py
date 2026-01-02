import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=LI()
    b=[0]*N
    
    
    for i in range(N-1,-1,-1):
        temp=0
        for j in range(i+1,N+1,i+1):
            jj=j-1
            if b[jj]:
                temp+=1
        temp=temp%2
        if temp!=a[i]:
            b[i]=1
            
    M=sum(b)
    ans=[]
    for i in range(N):
        if b[i]:
            ans.append(i+1)
            
    print(M)
    print(' '.join(map(str, ans)))
        

main()
