import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    from collections import deque
    
    N=I()
    A2=[0]*N
    for i in range(N):
        A2[i]=I()
        
    A2.sort(reverse=True)
    
    A=deque()
    B=deque()
    for i in range(N):
        A.append(A2[i])
        B.appendleft(A2[i])
    
    
    ans=0
    L=[0]*(2*N+1)
    L[N]=A.pop()
    l=N-1
    r=N+1
    
    for i in range(N-1):
        if i%4==0:
            a=A.popleft()
            L[l]=a
            ans+=abs(L[l]-L[l+1])
            l-=1
        elif i%4==1:
            a=A.popleft()
            L[r]=a
            ans+=abs(L[r]-L[r-1])
            r+=1
        elif i%4==2:
            a=A.pop()
            L[l]=a
            ans+=abs(L[l]-L[l+1])
            l-=1
        else:
            a=A.pop()
            L[r]=a
            ans+=abs(L[r]-L[r-1])
            r+=1
            
    ###
    ans2=0
    L=[0]*(2*N+1)
    L[N]=B.pop()
    l=N-1
    r=N+1
    
    for i in range(N-1):
        if i%4==0:
            a=B.popleft()
            L[l]=a
            ans2+=abs(L[l]-L[l+1])
            l-=1
        elif i%4==1:
            a=B.popleft()
            L[r]=a
            ans2+=abs(L[r]-L[r-1])
            r+=1
        elif i%4==2:
            a=B.pop()
            L[l]=a
            ans2+=abs(L[l]-L[l+1])
            l-=1
        else:
            a=B.pop()
            L[r]=a
            ans2+=abs(L[r]-L[r-1])
            r+=1
    ###        
    
    print(max(ans,ans2))
            
            
            
        
    
    
    

main()
