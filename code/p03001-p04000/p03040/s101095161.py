# ABC140E
import sys
input = sys.stdin.readline
def bsearch(target, min_i, max_i, func):
    # func(index) <= target < func(index+1) となるindexを返す
    if func(max_i) <= target:
        return max_i
    if target < func(min_i):
        return None
    index = (max_i + min_i)//2
    while True:
        if func(index) <= target:
            if target < func(index+1):
                return index
            index, min_i = (index+1 + max_i)//2, index+1
            continue
        index, max_i = (index-1 + min_i)//2, index-1

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

q=int(input())
xs = []
ys = []
qs = dict()
c = 0
for _ in range(q):
    xy = list(map(int,input().split()))
    if len(xy) == 1:
        if c not in qs:
            qs[c] = 0
        qs[c] += 1
    else:
        c += 1
        xs.append(xy[1])
        ys.append(xy[2])

N=len(xs)
sxs=sorted(xs)
zxs = [0]*N
for i, x in enumerate(sorted(range(N), key=lambda x : xs[x])):
    zxs[x] = i

seg_sum_tree = Bit(N)
seg_count_tree = Bit(N)

sy = 0
for i in range(c+1):
    if i in qs:
        x1i=bsearch(i//2 + (-1 if i % 2 == 0 else 0) ,0 ,N ,lambda x : seg_count_tree.sum(x))
#        print(x1i, i//2, seg_count_tree.query(0, 2))
        if i % 2:
        #print(sy, seg_sum_tree.query(0, x1i))
            r = sy - seg_sum_tree.sum(x1i) + \
                   seg_sum_tree.sum(N) - seg_sum_tree.sum(x1i+1)
        else:
            r = sy - seg_sum_tree.sum(x1i+1) + \
                   seg_sum_tree.sum(N) - seg_sum_tree.sum(x1i+1)
        for _ in range(qs[i]):
            print(sxs[x1i], r)
    if i == c:
        break
    x, y = xs[i], ys[i]
    xi = zxs[i]
    sy += y
    seg_sum_tree.add(xi+1, x)
    seg_count_tree.add(xi+1, 1)
