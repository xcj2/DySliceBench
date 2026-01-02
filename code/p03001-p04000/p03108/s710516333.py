import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size_dict = {i:1 for i in range(n)}
        self.fuben = n * (n-1) / 2

    def merge(self, i, j):
        rooti = self.findroot(i)
        rootj = self.findroot(j)
        if rooti == rootj:
          return
        self.parents[rooti] = rootj
        sj = self.size_dict[rootj]
        si = self.size_dict[rooti]
        self.fuben -= sj*(n-sj)/2
        self.fuben -= si*(n-si)/2
        self.fuben += (sj+si)*(n-(sj+si))/2
        self.size_dict[rootj] += self.size_dict[rooti]
        self.size_dict[rooti] = 0

    def issame(self, i, j):
        rooti = self.findroot(i)
        rootj = self.findroot(j)
        return rooti == rootj

    def findroot(self, i, followed_indices=None):

        if i == self.parents[i]:
            return i
        else:
            root = self.findroot(self.parents[i])
            self.parents[i] = root # 経路圧縮
            return root
          
n, m = LI()
edge_list = []
for i in range(m):
  a, b = LI()
  edge_list.append((a-1, b-1))
  
ans = []

uf = UnionFind(n)
import collections

for e in edge_list[::-1]:
  ans.append(int(uf.fuben))
  uf.merge(e[0], e[1])

for a in ans[::-1]:
  print(a)
