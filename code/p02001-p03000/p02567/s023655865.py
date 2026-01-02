class segtree:
    ## define what you want to do ,(min, max)
    sta = -1
    func = max

    def __init__(self,n):
        self.n = n
        self.tree = [self.sta]*(2*n)

    def build(self, list):
        for i,x in enumerate(list,self.n):
            self.tree[i] = x

        for i in range(self.n-1,0,-1):
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    def set(self,i,x):
        i += self.n
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    ## take the value of [l,r) 
    def get(self,l,r):
        l += self.n
        r += self.n
        res = self.sta

        while l < r:
            if l & 1:
                res = self.func(self.tree[l],res)
                l += 1
            if r & 1:
                res = self.func(self.tree[r-1],res)
            l >>= 1
            r >>= 1
        return res

    def max_right(self, l, x):
        """[l,r) が ok であるような最大の r を返す"""
        N = self.n
    
        def is_ok(v):
            return v < x
    
        def get_max(a,b):
            if a is None:
                return b
            if b is None:
                return a
            return max(a,b)
        v = None
        i, node_l, node_w = l + N, l, 1
        while True:
            if not (i & 1):
                i >>= 1
                node_w <<= 1
                continue
            if node_l + node_w > N:
                break
            v1 = get_max(v, self.tree[i])
            if is_ok(v1):
                v, i = v1, (i + 1) >> 1
                node_l, node_w = node_l + node_w, node_w << 1
            else:
                break
        # 奇数セルに居て、とりきれないことが分かっている。偶数をとっていく
        i, node_w = i << 1, node_w >> 1
        while node_w:
            if node_l + node_w > N:
                i, node_w = i << 1, node_w >> 1
                continue
            v1 = get_max(v, self.tree[i])
            if is_ok(v1):
                v, i = v1, (i + 1) << 1
                node_l, node_w = node_l + node_w, node_w >> 1
            else:
                i, node_w = i << 1, node_w >> 1
        i >>= 1
        return i - N


n,q = map(int,input().split())
a = list(map(int,input().split()))

seg = segtree(n)
seg.build(a)
for _ in range(q):
    t,x,v = map(int,input().split())
    if t == 1:
        seg.set(x-1,v)
    elif t == 2:
        print(seg.get(x-1,v))
    else:
        print(seg.max_right(x-1,v)+1)