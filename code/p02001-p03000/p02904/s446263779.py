import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
Ps = list(mapint())

def segfunc(x, y):
    return min(x, y)

def segfunc_2(x, y):
    return max(x, y)

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

if N==K:
    print(1)
    exit()
seg_min = SegTree(Ps, segfunc, 10**18)
seg_max = SegTree(Ps, segfunc_2, -1)

str_set = set()
cnt = 1
old = 10**18
is_increase = [0]*N
for i in range(N):
    p = Ps[i]
    if p>old:
        cnt += 1
        is_increase[i] = cnt
    else:
        cnt = 1
        is_increase[i] = cnt
    old = p

original = 0
ans = N-K+1
for i in range(N-K):
    mini = Ps[i]
    maxi = Ps[i+K]
    if is_increase[i+K-1]>=K:
        original = 1
        ans -= 1
    elif (seg_min.query(i, i+K+1)==mini and seg_max.query(i, i+K+1)==maxi):
        ans -= 1
if is_increase[-1]>=K:
    original = 1
    ans -= 1
print(ans+original)