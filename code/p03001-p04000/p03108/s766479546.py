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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, M = map(int, input().split())
    bridge = []
    uni = UnionFind(N)
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        bridge.append([A,B])
    cnt = N * (N - 1) // 2
    ans = [cnt]
    for i in range(M-1,-1,-1):
        A, B = bridge[i]
        if uni.same(A,B):
            ans.append(cnt)
        else:
            cnt -= uni.size(A) * uni.size(B)
            ans.append(cnt)
            uni.union(A,B)
    for i in range(M-1,-1,-1):
        print(ans[i])



if __name__ == "__main__":
    main()