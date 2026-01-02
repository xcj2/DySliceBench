class SegmentTree:
    def __init__(self, lst, op, e):
        self.n = len(lst)
        self.N = 1 << ((self.n - 1).bit_length())
        self.op = op # operation
        self.e = e # identity element
        self.v = self._build(lst) # self.v is set to be 1-indexed for simplicity
        
    def _build(self, lst):
        # construction of a tree
        # total 2 * self.N elements (tree[0] is not used)
        tree = [self.e] * (self.N) + lst + [self.e] * (self.N - self.n)
        for i in range(self.N - 1, 0, -1): tree[i] = self.op(tree[i << 1], tree[(i << 1)|1])
        return tree
    
    def __getitem__(self, i):
        return self.v[i + self.N]
    
    # update a_i to be x 
    def update(self, i, x):
        v, op = self.v, self.op
        i += self.N
        v[i] = x
        while i > 0:
            i >>= 1 # move to parent
            v[i] = op(v[i << 1], v[(i << 1)|1])
    
    # returns answer for the query interval [l, r)
    def fold(self, l, r):
        N, e, v, op = self.N, self.e, self.v, self.op
        left = l + N; right = r + N
        L = R = e
        while left < right:
            if left & 1: # self.v[left] is the right child
                L = op(L, v[left])
                left += 1
            if right & 1: # self.v[right-1] is the left child
                right -= 1
                R = op(v[right], R)
            left >>= 1; right >>= 1
        return op(L, R)

def wa(set1, set2):
    return set1 | set2

n = int(input())
s = input()
lst = []
for i in range(n):
    lst.append(set([s[i]]))

st = SegmentTree(lst, wa, set([]))

ans = []
q = int(input())
for i in range(q):
    que = input()
    if que[0] == '1':
        kind, i, c = que.split()
        i = int(i) - 1
        st.update(i, set([c]))
    else:
        kind, l, r = map(int, que.split())
        l -= 1
        ans.append(len(st.fold(l, r)))

for i in ans:
    print(i)