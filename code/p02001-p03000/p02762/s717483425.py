import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10000)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]
        
def resolve():
    N, M, K = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    C = [0]*K
    D = [0]*K
    for i in range(K):
        C[i], D[i] = map(int, input().split())

    uf = UnionFind(N)
    for a, b in zip(A, B):
        uf.union(a-1, b-1)

    direct_friends_num = [0]*N
    for a, b in zip(A, B):
        direct_friends_num[a-1] += 1
        direct_friends_num[b-1] += 1
    blocked_num = [0]*N
    for c, d in zip(C, D):
        if uf.find(c-1) == uf.find(d-1):
            blocked_num[c-1] += 1
            blocked_num[d-1] += 1

    ans = [0]*N
    for i in range(N):
        ans[i] = uf.size(i) - direct_friends_num[i] - blocked_num[i] - 1
    print(*ans)

if __name__ == '__main__':
    resolve()
