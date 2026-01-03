import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    W,H,N=MI()
    L=[0,W,0,H]
    for _ in range(N):
        x,y,a=MI()
        a-=1
        if a==0:
            L[a]=max(L[a],x)
        elif a==1:
            L[a]=min(L[a],x)
        elif a==2:
            L[a]=max(L[a],y)
        else:
            L[a]=min(L[a],y)
            
            
    dx=L[1]-L[0]
    dy=L[3]-L[2]
    
    if dx>0 and dy>0:
        print(dx*dy)
    else:
        print(0)
            

main()
