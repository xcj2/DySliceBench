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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        bridges.append((A,B))

    ans = [0] * M
    ans[M-1] = N * (N - 1) // 2
    uni = UnionFind(N)
    for i in range(M-1,0,-1):
        a, b = bridges[i]
        if not uni.same(a, b):
            ans[i-1] = ans[i] - (uni.size(a) * uni.size(b))           
            uni.union(a,b)
        else:
            ans[i-1] = ans[i]
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()