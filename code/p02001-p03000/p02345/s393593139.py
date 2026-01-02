class SegTreeNode:
    def __init__(self, value = 0, l = 0, r = 0, lson = None, rson = None):
        self.value = value
        self.l = l
        self.r = r
        self.lson = lson
        self.rson = rson

class SegTree:
    MIN_NUMBER = 0
    MAX_NUMBER = 2**31 - 1
    def __init__(self, l, r):
        self.root = self.build(l, r)
    
    def build(self, l, r):
        if l > r:
            return None
        root = SegTreeNode(self.MAX_NUMBER, l, r)
        if l == r:
            return root
        mid = (l + r) >> 1
        root.lson = self.build(l, mid)
        root.rson = self.build(mid+1, r)
        return root
    
    def __update(self, root, l, r, value):
        if l > root.r or r < root.l or root == None:
            return
        if l <= root.l and root.r <= r:
            root.value = value
            return
        self.__update(root.lson, l, r, value)
        self.__update(root.rson, l, r, value)
        root.value = min(root.lson.value, root.rson.value)
    
    def update(self, i, value):
        self.__update(self.root, i, i, value)

    def __query(self, root, l, r):
        if l > root.r or r < root.l or root == None:
            return SegTree.MAX_NUMBER
        if l <= root.l and root.r <= r:
            return root.value
        return min(self.__query(root.lson, l, r), self.__query(root.rson, l, r))

    def query(self, l, r):
        return self.__query(self.root, l, r)

n, q = map(int, input().split())
seg = SegTree(0, n)
while q:
    q -= 1
    op, l, r = map(int, input().split())
    if op == 0:
        seg.update(l, r)
    else:
        print(seg.query(l, r))
