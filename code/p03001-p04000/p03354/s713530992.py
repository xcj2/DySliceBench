import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for _ in range(m)]

    class UnionFind(object):
        def __init__(self, n=1):
            self.par = [i for i in range(n)]
            self.rank = [0 for _ in range(n)]
            self.size = [1 for _ in range(n)]

        def find(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x != y:
                if self.rank[x] < self.rank[y]:
                    x, y = y, x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
                self.par[y] = x
                self.size[x] += self.size[y]

        def all_group_members(self):
            return_list = [list() for i in range(n)]
            for i in range(n):
              return_list[self.find(i)].append(i)
            return return_list

    uf = UnionFind(n)
    ans = 0
    for x,y in xy:
        uf.union(x-1,y-1)
    for v in uf.all_group_members():
        set1 = set()
        for i in v:
            set1.add(p[i]-1)
        ans += len(set(v)&set1)

    print(ans)

if __name__ == '__main__':
    main()
