import sys
sys.setrecursionlimit(10**9)


class UnionFind():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

def main():
    N,M = mi()
    U = UnionFind(2*N+1)

    for i in range(1,N+1):
        U.unite(i,N+i)

    minus = 0
    for i in range(M):
        x,y,z = mi()
        U.unite(x,y)

    print(U.calc_group_num() - 1)




if __name__ == "__main__":
  main()
