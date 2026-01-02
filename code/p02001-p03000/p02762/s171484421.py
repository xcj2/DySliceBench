#!/usr/bin/env python3

class UnionFind():
        def __init__(self, n):
            self.parents = list(range(n))
            self.size = [1] * n
    
        def find(self, x):
            if self.parents[x] == x:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
    
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x != y:
                if self.size[x] < self.size[y]:
                    x, y = y,x
                self.parents[y] = x
                self.size[x] += self.size[y]

def main():
    N, M, K = map(int, input().split())
    friend_adj = [[] for _ in range(N)]
    block_adj = [[] for _ in range(N)]
    uf = UnionFind(N)

    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        friend_adj[a].append(b)
        friend_adj[b].append(a)
        uf.union(a,b)
    for _ in range(K):
        c, d = map(lambda x: int(x)-1, input().split())
        if uf.find(c) == uf.find(d):
            friend_adj[c].append(d)
            friend_adj[d].append(c)

    ans = [uf.size[uf.find(i)]-1 for i in range(N)]

    for i in range(N):
        ans[i] -= len(friend_adj[i])        
        # for b in block_adj[i]:
        #     if uf.find(b) == uf.find(i):
        #         ans[i] -= 1
    print(*ans)
    
    
    

if __name__ == "__main__":
    main()
