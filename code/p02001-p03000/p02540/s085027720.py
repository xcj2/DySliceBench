from bisect import bisect_left
from collections import Counter
import sys

def main():
    input = sys.stdin.readline
    N = int(input().rstrip())
    # Union-Find
    parent = list(range(N))
    rank = [1] * N
    def get_root(node):
      if parent[node] == node:
        return node
      root = get_root(parent[node])
      parent[node] = root
      return root
    
    def union(a, b):
      root_a = get_root(a)
      root_b = get_root(b)
      if root_a == root_b:
        return
      rank_a = rank[root_a]
      rank_b = rank[root_b]
      if rank_a < rank_b:
        parent[root_a] = root_b
      else:
        parent[root_b] = root_a
        if rank_a == rank_b:
          rank[root_a] += 1

    XYs = []
    XYs1 = []
    XYs2 = []
    for i in range(N):
        x, y = map(int, input().rstrip().split())
        XYs.append([x, y, i])
        XYs2.append([N-x, N-y, i])
    XYs1 = sorted(XYs)
    XYs2.sort()
    
    buf = []
    L = 0
    for x, y, k in XYs1:
        idx = bisect_left(buf, [-y, k])
        if idx == L:
            buf.append([-y, k])
        else:
            ny, nk = buf[-1]
            while L > idx:
                ty, tk = buf.pop()
                union(k, tk)
                L -= 1
            buf.append([ny, nk])
        L += 1
    
    buf = []
    L = 0
    for x, y, k in XYs2:
        idx = bisect_left(buf, [-y, k])
        if idx == L:
            buf.append([-y, k])
        else:
            ny, nk = buf[-1]
            while L > idx:
                ty, tk = buf.pop()
                union(k, tk)
                L -= 1
            buf.append([ny, nk])
        L += 1

    ct = Counter()
    for i in range(N):
        ct[get_root(i)] += 1
    
    for p in parent:
        print(ct[p])

main()
