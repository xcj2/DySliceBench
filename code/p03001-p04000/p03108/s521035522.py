import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# BEGIN CUT HERE
class UnionFind():
    def __init__(self,n):
        self.data = [-1] * n
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.data[x] < self.data[y]:
            x, y = y, x  # swap
        self.data[x] += self.data[y]
        self.data[y] = x
    
    def find(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.find(self.data[x])
        return self.data[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return self.data[self.find(x)]
        
# END CUT HERE

def ABC120_D():
    n, m = mi()
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = mi()
        
    uf = UnionFind(n)
    ans = [0] * (m + 1)
    ans[m] = n * (n - 1) // 2

    for i in range(m - 1, -1, -1):
        a[i] -= 1
        b[i] -= 1
        ans[i] = ans[i + 1]
        if uf.same(a[i], b[i]):
            continue
        
        x = uf.size(a[i])
        y = uf.size(b[i])
        ans[i] -= x * y
        
        uf.unite(a[i],b[i])
    
    for i in range(1, m + 1):
        print(ans[i])



if __name__ == '__main__':
    ABC120_D()
