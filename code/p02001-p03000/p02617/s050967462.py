import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    # 連結成分の数は，頂点すう - 辺数
    mod=10**9+7
    N=I()
    # 頂点が数えられる回数　Σ(i*(N-i+1))
    ans=N*(N+1)//2+(N*(N-1)*(N+1))//6
    for i in range(N-1):
        u,v=MI()
        if u>v:
            u,v=v,u
            
        #辺uvを含むくみが何通りあるか
        ans-=(u)*(N-v+1)

        
    print(ans)
                
        
    

main()
