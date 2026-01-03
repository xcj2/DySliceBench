import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

    

def main():
    mod=10**9+7
    N,M=MI()
    edges=[None]*M
    
    for i in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        c*=-1
        edges[i]=(a,b,c)
        
    ########################    
    #0から他の頂点へ
    def BellmanFord(N, M, edges):
        inf=10**20
        d = [inf] * N
        d[0] = 0

        for i in range(N-1):
            for (u, v, c) in edges:
                if d[u] + c < d[v]:
                    d[v] = d[u] + c

        #for i in range(N):
        for (u, v, c) in edges:
            if d[u] + c < d[v]:
                if v == N-1:
                    return None#負の閉路
                
                d[v] = d[u] + c
        return d[N-1]
    ########################
        
    ans = BellmanFord(N, M, edges)
    if ans is None:
        print('inf')
    else:
        print(-ans)

main()
