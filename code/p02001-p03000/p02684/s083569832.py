import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    for i in range(N):
        A[i]-=1
    used=[0]*N
    used[0]=1
    
    now=0
    nxt=0
    cnt=1
    flag=1
    while True:
        nxt=A[now]
        if used[nxt]==0:
            used[nxt]=cnt+1
        else:
            if flag:
                lpath=cnt+1-used[nxt]
                roop=(K-cnt)//lpath
                #print(lpath,roop,cnt)
                cnt+=roop*lpath
                flag=0
        now=nxt
        #print(now,cnt)
        if cnt==K:
            break
        cnt+=1
        
            
    print(now+1)

main()
