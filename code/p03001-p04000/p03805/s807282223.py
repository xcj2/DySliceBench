import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
import itertools

def main():
    mod=10**9+7
    N,M=MI()
    adj=[[] for _ in range(N)]
    for _ in range(M):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
        
        
    ans=0
    for ite in itertools.permutations(range(1,N), N-1):
        v=0
        f=1
        for nv in ite:
            if nv in adj[v]:
                v=nv
            else:
                f=0
                break
        ans+=f
        
    print(ans)
        
            
    

main()
