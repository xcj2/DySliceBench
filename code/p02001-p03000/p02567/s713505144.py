class SegmentTree:
    def __init__(self, n, func=lambda x, y : max(x, y), default_val = -float('inf'), init_list = None):
        assert n > 0 and (not init_list or len(init_list) <= n)
        self.n = n
        self.leaf_n = 1
        while n > self.leaf_n:
            self.leaf_n <<= 1
        self.node_n = (self.leaf_n << 1) - 1
        self.offset = self.leaf_n - 1
        self.tree = [default_val] * self.node_n
        self.default_val = default_val
        self.f = func

        if init_list:
            self.tree[self.offset:self.offset+n] = init_list
            self.update_all()
    
    def set_values(self, val_list):
        n = len(val_list)
        assert self.leaf_n >= n
        self.tree[self.offset:self.offset+n] = val_list
    
    def set_value(self, index, val):
        assert 0 <= index < self.leaf_n
        self.tree[self.offset+index] = val

    def get_value(self, index):
        assert 0 <= index < self.leaf_n
        return self.tree[self.offset + index]

    def update_all(self):
        l = self.offset
        n = self.leaf_n
        while l > 0:
            for i in range(l, l + n, 2):
                self.tree[i>>1] = self.f(self.tree[i], self.tree[i+1])
            l >>= 1
            n >>= 1

    def update(self, index, val):
        assert 0 <= index < self.leaf_n
        i = self.offset + index
        self.tree[i] = val
        while i > 0:
            if i & 1 == 0:
                i -= 1
            self.tree[i>>1] = self.f(self.tree[i], self.tree[i+1])
            i >>= 1
    # 閉区間 [l, r] の演算結果
    def query(self, l, r):
        assert 0 <= l <= r < self.leaf_n
        left_val = self.default_val
        right_val = self.default_val
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1 == 0:
                left_val = self.f(left_val, self.tree[l])
            if r & 1 == 1:
                right_val = self.f(self.tree[r], right_val)
                r -= 1
            l >>= 1
            r = (r >> 1) - 1
        if l == r:
            left_val = self.f(left_val, self.tree[l])
        return self.f(left_val, right_val)

    def search_max_right(self, l, check_func):
        '''
        閉区間 [l, r] の演算結果 x が check_func(x) == True となるような最大の r を返す。存在しない場合-1を返す。
        -------
        例：最大値がv以下になる区間を探す
            f = max
            check_func = lambda(x):x <= v
        '''
        assert(0 <= l < self.leaf_n and check_func(self.default_val))
        i = l + self.offset
        if not check_func(self.tree[i]):
            return -1
        left_val = self.default_val
        while True:
            while i & 1 != 0: # iを左端とする最上の層まで移動
                i >>= 1
            x = self.f(left_val, self.tree[i])
            if not check_func(x):
                while i < self.offset:
                    i = (i << 1) + 1 #iを左端とする1個下の層に移動
                    x = self.f(left_val, self.tree[i])
                    if check_func(x):
                        left_val = x
                        i += 1
                return i - self.offset - 1
            left_val = x
            i += 1
            if i & (i + 1) == 0:
                return self.n - 1

    def search_min_left(self, r, check_func):
        '''
        閉区間 [l, r] の演算結果 x が check_func(x) == True となるような最小の l を返す。
        -------
        例：最大値がv以下になる区間を探す
            f = max
            check_func = lambda(x): x <= v
        '''
        assert(0 <= r < self.leaf_n and check_func(self.default_val))
        i = r + self.offset
        if not check_func(self.tree[i]):
            return -1
        right_val = self.default_val
        while True:
            while i & 1 == 0 and i > 0: # iを右端とする最上の層まで移動
                i = (i - 1) >> 1
            x = self.f(self.tree[i], right_val)
            if not check_func(x):
                while i < self.offset:
                    i = (i + 1) << 1 #iを右端とする1個下の層に移動
                    x = self.f(self.tree[i], right_val)
                    if check_func(x):
                        right_val = x
                        i -= 1
                return i - self.offset + 1
            right_val = x
            if i & (i + 1) == 0:
                return 0
            i -= 1

n, q = map(int, input().split())
a = list(map(int, input().split()))

st = SegmentTree(n, max, 0, a)
ans = []
for _ in range(q):
    t, x, v = map(int, input().split())
    if t == 1:
        st.update(x-1, v)
    elif t == 2:
        ans.append(st.query(x-1, v-1))
    else:
        if v == 0:
            ans.append(x)
        else:
            i = st.search_max_right(x - 1, lambda y: y < v)
            ans.append(x if i < 0 else i + 2)
for x in ans:
    print(x)