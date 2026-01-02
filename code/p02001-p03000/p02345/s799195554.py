#普通のセグ木
'''
org: 配列[list]
func: 関数 (min,max,sumなど)
unit: 初期値
'''
class SegmentTree:
    def __init__(self, orig, func, unit):
        _len = len(orig)
        self.func = func
        self.size = 1 << (_len - 1).bit_length()
        self.tree = [unit] * self.size + orig + [unit] * (self.size - _len)
        self.unit = unit

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i, v):
        i += self.size
        self.tree[i] = v
        while i:
            i //= 2
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])
    # l <= x <r
    def find(self, l, r):
        l += self.size
        r += self.size
        ret = self.unit
        while l < r:
            if l & 1:
                ret = self.func(ret, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.func(ret, self.tree[r])
            l //= 2
            r //= 2
        return ret

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,q = mi()
seg = SegmentTree([(1<<31) -1]*n,min,(1<<31) -1)
for _ in range(q):
    a,b,c = mi()
    if a == 1:
        print(seg.find(b,c+1))
    else:
        seg.update(b,c)

