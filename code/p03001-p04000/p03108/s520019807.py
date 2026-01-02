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
    from sys import stdin
    from collections import deque
    input = lambda: stdin.readline()
    N,M = map(int,input().split())
    uf = UnionFind(N+1)
    AB = deque()
    for i in range(M):
        AB.append(map(int,input().split()))
    diff_pairs = [0]*M
    AB.reverse()
    prev = 0
    for i,(a,b) in enumerate(AB):
        if not uf.same(a,b):
            num_a = uf.size(a)
            num_b = uf.size(b)
            prev += num_a * num_b
            uf.union(a,b)
        diff_pairs[M-i-1] = prev
    outputs = deque()
    sum_d = 0
    prev = diff_pairs[0]
    for i in range(1,M):
        sum_d += prev-diff_pairs[i]
        outputs.append(sum_d)
        prev = diff_pairs[i]
    outputs.append(sum_d+1)
    print('\n'.join(map(str,outputs)))



main()