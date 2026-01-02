from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.parent = [-1]*n
    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    def union(self, x,y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return False
        # root_xのほうが要素が多い
        if self.parent[root_x] < self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
        return True
    def lists(self):
        d = defaultdict(list)
        for i in range(len(self.parent)):
            parent = self.root(i)
            d[parent].append(i)
        return d

def main():
    n, m = map(int, input().split())
    ps = list(map(int, input().split()))
    UF = UnionFind(n)
    for i in range(m):
        x, y = list(map(int, input().split()))
        UF.union(x-1, y-1)
    ans = 0
    for indices in UF.lists().values():
        indices_set = set(indices)
        p_set = set(ps[i]-1  for i in indices)
        ans += len(p_set & indices_set)
    print(ans)
if __name__ == '__main__':
    main()