import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=[0]*N
    for i in range(N):
        a[i]=I()
        
    used=[0]*N
    used[0]=1
    now=0
    cnt=0
    f=0
    for i in range(N):
        cnt+=1
        now=a[now]-1
        if now==1:
            f=1
            break
        if used[now]==1:
            break
        used[now]=1
        
    if f==1:
        print(cnt)
    else:
        print(-1)

main()
