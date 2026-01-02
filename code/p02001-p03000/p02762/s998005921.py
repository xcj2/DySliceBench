#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


# refered to
# rank : http://at274.hatenablog.com/entry/2018/02/02/173000
# size : abc120 kaisetsu
class UnionFind:
    def __init__(self, n):
        # par = Parent Number or NoV
        self.par = [-1] * (n+1)
        # rank = Tree Height
        self.rank = [0] * (n+1)
    
    # Returns the number of sets to which x belongs
    def size(self, x):
        return -1*self.par[self.find(x)]
    
    def size_list(self):
        return [x*(-1) for x in self.par[1:] if x < 0]

    # Returns number if root
    def find(self, x):
        if(self.par[x] < 1):
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    # Are the parents of x and y the same?
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        # find root 
        x = self.find(x)
        y = self.find(y)

        # Already x connect to y
        if(x == y):
            return False

        # Reconnect
        if(self.size(x) < self.size(y)):
            x,y = y,x
        
        # update x size
        self.par[x] += self.par[y]
        # set parent number of y to x
        self.par[y] = x

        return True 
    
    def root_nodes(self):
        return len([i for i in self.par[1:] if i <= -1])
    
    

def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    """graph.input.linkedlist
        input: u[]:start, v[]:end
        output:g[][]
    """
    uf = UnionFind(N)

    g = [[] for i in range(N+1)]
    for i in range(M):
        g[A[i]].append(B[i])
        g[B[i]].append(A[i])
    
    g_b = [[] for i in range(N+1)]
    for i in range(K):
        g_b[C[i]].append(D[i])
        g_b[D[i]].append(C[i])
    

    for i in range(M):
        uf.union(A[i], B[i])

    ans = []
    for i in range(1, N+1):
        ans.append(uf.size(i)-1 - len(g[i]) - len([x for x in g_b[i] if uf.same_check(i, x) == True]))
        
    print(' '.join(map(str, ans)))
    
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, K, A, B, C, D)

if __name__ == '__main__':
    main()
