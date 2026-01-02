import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# PyPyだと再帰が遅いので注意
# BEGIN CUT HERE
sys.setrecursionlimit(100000)
class UnionFind():
    '''UnionFind木'''
    def __init__(self,n):
        self.data = [-1] * n
    
    def unite(self, x, y):
        '''x と y を結合'''
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.data[x] < self.data[y]:
            x, y = y, x  # swap
        self.data[x] += self.data[y]
        self.data[y] = x
    
    def find(self, x):
        '''ノード x の親を返す'''
        if self.data[x] < 0:
            return x
        self.data[x] = self.find(self.data[x])
        return self.data[x]

    def same(self, x, y):
        '''x と y が同じグループに属するか判定'''
        return self.find(x) == self.find(y)
    
    def size(self, x):
        '''x を含むグループのノード数を返す'''
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

# verified on 2019/06/23
# Python3:616ms https://atcoder.jp/contests/abc120/submissions/6094323

def ABC126_E():
    N, M = mi()
    uf = UnionFind(N)
    for i in range(M):
        _X, _Y, _Z = mi()
        uf.unite(_X - 1, _Y - 1)
    ans = 0
    for i in range(N):
        if uf.find(i) == i:
            ans += 1
    print(ans)


if __name__ == '__main__':
    # ABC120_D()
    ABC126_E()