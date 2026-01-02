import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=[0]*N
    xy=[]
    for i in range(N):
        A[i]=I()
        temp=[]
        for _ in range(A[i]):
            x,y=MI()
            x-=1
            temp.append((x,y))
        xy.append(temp)
        
    import itertools
    ans=0
    
    for ite in itertools.product([0,1], repeat=N):
        # ite[i]=1なら正直者，
        flag=1
        for i in range(N):
            if flag==0:
                break
            if ite[i]==1:
                for x,y in xy[i]:
                    if ite[x]!=y:
                        flag=0
                        break
        if flag:
            ans=max(ans,sum(ite))
            
    print(ans)
            

main()
