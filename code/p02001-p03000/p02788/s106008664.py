import bisect
from math import ceil
class BinaryIndexedTree():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        self.depth = self.size.bit_length()
 
    def initialize(self, seq):
        for i, x in enumerate(seq[1:], 1):
            self.tree[i] += x
            j = i + (i & (-i))
            if j < self.size:
                self.tree[j] += self.tree[i]
 
    def __repr__(self):
        return self.tree.__repr__()
 
    def get_sum(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i
 
    def find_kth_element(self, k):
        x, sx = 0, 0
        dx = (1 << self.depth)
        for i in range(self.depth - 1, -1, -1):
            dx = (1 << i)
            if x + dx >= self.size:
                continue
            y = x + dx
            sy = sx + self.tree[y]
            if sy < k:
                x, sx = y, sy
        return x + 1

n,d,a = map(int,input().split())
monster = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])
x_list = [0]+[monster[i][0] for i in range(n)]+[float("inf")]
h_list = [0]+[monster[i][1] for i in range(n)]+[float("inf")]

bit = BinaryIndexedTree(n+2)
ans = 0
for i in range(1,n+1):
    hp = h_list[i] - bit.get_sum(i)
    if hp < 0:
        continue
    atk_time = ceil(hp/a)
    ans += atk_time
    top = bisect.bisect_right(x_list, x_list[i]+2*d)
    bit.add(i, atk_time*a)
    bit.add(top, -atk_time*a)

print(ans)