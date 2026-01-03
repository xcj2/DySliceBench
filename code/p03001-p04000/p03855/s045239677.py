from collections import Counter

class UnionFind:
    __slots__ = ['id']
    def __init__(self, n):
        self.id = [-1] * n
    def find(self, x):
        if self.id[x] < 0:
            return x
        else:
            self.id[x] = self.find(self.id[x])
            return self.id[x]
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.id[s1] <= self.id[s2]:
                self.id[s1] += self.id[s2]
                self.id[s2] = s1
            else:
                self.id[s2] += self.id[s1]
                self.id[s1] = s2
            return True
        return False
    def subsetall(self):
        a = []
        for i in range(len(self.id)):
            if self.id[i] < 0:
                a.append((i, -self.id[i]))
        return a

if __name__ == '__main__':
    N, K, L = map(int, input().split())

    uf_K = UnionFind(N)
    uf_L = UnionFind(N)
    for _ in [0] * K:
        p, q = map(int, input().split())
        uf_K.union(p - 1, q - 1)
    for _ in [0] * L:
        r, s = map(int, input().split())
        uf_L.union(r - 1, s - 1)

    keys, d = [], Counter()
    for i in range(N):
        key = uf_K.find(i), uf_L.find(i)
        keys.append(key)
        d[key] += 1

    print(*(d[key] for key in keys))