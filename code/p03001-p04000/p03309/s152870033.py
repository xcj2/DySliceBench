class SplayNode:
    """Splay木のノードを定義
    メンバ変数: 値、サイズ、親へのポインタ、左右の子へのポインタ
    """
    def __init__(self, val):
        self.val = val
        self.size = 1
        self.parent, self.right, self.left = None, None, None


class SplayTree:
    """Splay木を定義"""
    def __init__(self):
        self.root = None

    def __getitem__(self, ind: int):  # O(logN)
        return self.get_ptr(ind, self.root).val
        
    def __setitem__(self, ind: int, val):  # O(logN)
        ptr = self.get_ptr(ind, self.root)
        ptr.val = val

    def __len__(self):  # O(1)
        return self.root.size if self.root is not None else 0

    def update(self, ptr):
        """部分木の情報を更新する"""
        ptr.size = 1
        if ptr.left is not None:
            ptr.size += ptr.left.size
        if ptr.right is not None:
            ptr.size += ptr.right.size

    def state(self, ptr):
        """スプレー操作を行うときの状況判定
        親が存在しない: 0
        左の兄弟が存在する: 1
        右の兄弟が存在する: -1
        """
        if ptr.parent is None:
            return 0
        if ptr.parent.left == ptr:
            return 1
        if ptr.parent.right == ptr:
            return -1

    def splay(self, ptr):
        """ptrが根になるようにスプレー操作を行う"""
        while self.state(ptr) != 0:
            if self.state(ptr.parent) == 0:
                # zigステップ
                self.rotate(ptr)
            elif self.state(ptr) == self.state(ptr.parent):
                # zig-zigステップ
                self.rotate(ptr.parent)
                self.rotate(ptr)
            else:
                # zig-zagステップ
                self.rotate(ptr)
                self.rotate(ptr)
        self.root = ptr

    def rotate(self, ptr):
        """木の回転を行う"""
        p = ptr.parent
        pp = p.parent
        if p.left == ptr:
            c = ptr.right
            ptr.right = p
            p.left = c
        else:
            c = ptr.left
            ptr.left = p
            p.right = c
        if pp is not None and pp.left == p: pp.left = ptr
        if pp is not None and pp.right == p: pp.right = ptr
        ptr.parent = pp
        p.parent = ptr
        if c is not None:
            c.parent = p
        self.update(p)
        self.update(ptr)

    def get_ptr(self, ind, root):
        """ind番目のポインタを取得する"""
        ptr = root
        while True:
            if ptr.left is None:
                l_size = 0
            else:
                l_size = ptr.left.size
            if ind < l_size:
                ptr = ptr.left
            if ind == l_size:
                self.splay(ptr)
                return ptr
            if ind > l_size:
                ptr = ptr.right
                ind = ind - l_size - 1

    def merge(self, lroot, rroot):
        if lroot is None:
            self.root = rroot
            return rroot
        if rroot is None:
            self.root = lroot
            return lroot
        lroot = self.get_ptr(lroot.size - 1, lroot)
        lroot.right = rroot
        rroot.parent = lroot
        self.update(lroot)
        return lroot
      
    def split(self, left_cnt, root):
        if left_cnt == 0:
            return None, root
        if left_cnt == root.size:
            return root, None
        root = self.get_ptr(left_cnt, root)
        lroot = root.left
        rroot = root
        rroot.left = None
        lroot.parent = None
        self.update(rroot)
        return lroot, rroot
      
    def insert(self, ind, val):
        """ind番目の値valの要素を挿入する"""
        lroot, rroot = self.split(ind, self.root)
        new_ptr = SplayNode(val)
        self.merge(self.merge(lroot, new_ptr), rroot)
    
    def delete(self, ind):
        """indの要素を削除する"""
        root = self.get_ptr(ind, self.root)
        lroot = root.left
        rroot = root.right
        if lroot is not None:
            lroot.parent = None
        if rroot is not None:
            rroot.parent = None
        root.relf = None
        root.left = None
        self.update(root)
        return self.merge(lroot, rroot), root

    def add(self, val):
        if self.root is None:
            self.insert(0, val)
            return
        ptr = self.root 
        ind = 0
        while True:
            if val < ptr.val:
                if ptr.left is None:
                    self.insert(ind, val)
                    return
                ptr = ptr.left
            else:
                ind += 1
                if ptr.left is not None:
                    ind += ptr.left.size
                if ptr.right is None:
                    self.insert(ind, val)
                    return
                ptr = ptr.right


n = int(input())
a = list(map(int,input().split()))

sp = SplayTree()
for i in range(n)[::-1]:
    sp.insert(0, a[i])
for i in range(n):
    sp[i] = sp[i] - (i + 1)

ave = sorted([sp[i] for i in range(n)])[n // 2]
ans = 0

for i in range(n):
  ans += abs(sp[i] - ave)
  
print(ans)