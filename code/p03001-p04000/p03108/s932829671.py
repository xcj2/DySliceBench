import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)

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
    def same(self, x, y):
        return self.find(x) == self.find(y)
def main():
    N, M = map(int, readline().split())
    uf = UnionFind(N)
    AB = []
    for _ in range(M):
        a, b = map(int, readline().split())
        AB.append((a,b))
    ans = [N*(N-1)//2]
    for i in range(M-1,-1,-1):
        a,b = AB[i][0], AB[i][1]
        if uf.same(a-1,b-1):
            ans.append(ans[-1])
        else:
            tmp = ans[-1] - uf.size(a-1)*uf.size(b-1)
            ans.append(tmp)
            uf.union(a-1,b-1)
    for i in range(M-1,-1,-1):
        print(ans[i])
if __name__ == '__main__':
    main()