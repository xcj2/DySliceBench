import bisect


class UnionFind():
    
    def __init__(self, n):
        self.n = next
        self.parent = [-1 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        else:
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            return True
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parent[self.find(x)]
    
    def __str__(self):
        return str(self.parent)



def read():
    N, M, K = list(map(int, input().strip().split()))
    uf = UnionFind(N)
    friends = [list() for i in range(N+1)]
    blocked = [list() for i in range(N+1)]
    for i in range(M):
        a, b = list(map(int, input().strip().split()))
        friends[a].append(b)
        friends[b].append(a)
        uf.unite(a-1, b-1)
    for i in range(K):
        c, d = list(map(int, input().strip().split()))
        blocked[c].append(d)
        blocked[d].append(c)
    return N, M, K, friends, blocked, uf


def solve(N, M, K, friends, blocked, uf):
    n_friendships = [0 for i in range(N)]
    for i in range(1, N+1):
        n = uf.size(i-1)
        m = len(friends[i])
        k = 0
        for b in blocked[i]:
            if uf.same(i-1, b-1):
                k += 1
        n_friendships[i-1] = n-1-m-k
    return ' '.join(map(str, n_friendships))


if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
