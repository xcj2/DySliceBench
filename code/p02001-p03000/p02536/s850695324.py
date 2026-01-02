class UnionFind:
    __slots__ = ["_data_size", "_roots"]
 
    def __init__(self, data_size: int) -> None:
        self._data_size = data_size
        self._roots = [-1] * data_size
 
    def __getitem__(self, x: int) -> int:
        while self._roots[x] >= 0:
            x = self._roots[x]
        return x
 
    def is_connected(self, x: int, y: int) -> bool:
        return self[x] == self[y]
 
    def unite(self, x: int, y: int) -> None:
        x, y = self[x], self[y]
        if x == y:
            return
        if self._roots[x] > self._roots[y]:
            x, y = y, x
        self._roots[x] += self._roots[y]
        self._roots[y] = x
 
 
import sys
 
readline = sys.stdin.readline
 
N, Q = map(int, readline().split())
tree = UnionFind(N)
res = []
ans=0
for _ in range(Q):
  u, v = map(int, readline().split())
  tree.unite(u-1, v-1)
for u in range(1,N):
  if not tree.is_connected(u, 0):
      ans+=1
      tree.unite(u, 0)
print(ans)
