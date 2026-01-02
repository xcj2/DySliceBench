from random import random


class TreapNode:
    """Treapのノード定義
    メンバ変数: 値、優先度、親へのポインタ、左右の子へのポインタ"""
    def __init__(self, val):
        self.val = val
        self.priority = random()
        self.parent, self.right, self.left = None, None, None


class Treap:
    """平衡二分探索木: 値の検索、挿入、削除などクエリ処理をO(logN)で実行する"""
    def __init__(self, is_multiset=False):
        self.is_multiset = is_multiset
        self.root = None

    def search(self, val: int) -> bool:
        """値の検索: 集合に値valを持つノードが存在するか"""
        ptr = self.root
        while ptr is not None:
            if val < ptr.val:
                ptr = ptr.left
            elif val > ptr.val:
                ptr = ptr.right
            else:
                return True
        return False

    def insert(self, val: int) -> bool:
        """値の削除: 集合に値valを持つノードを挿入する"""
        if self.root is None:
            self.root = TreapNode(val)
            return True

        # ノードの挿入
        ptr = self.root 
        while True:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = TreapNode(val)
                    ptr.left.parent = ptr
                    ptr = ptr.left
                    break
                ptr = ptr.left
            else:
                if val == ptr.val and not self.is_multiset:
                    return False
                elif ptr.right is None:
                    ptr.right = TreapNode(val)
                    ptr.right.parent = ptr
                    ptr = ptr.right
                    break
                ptr = ptr.right

        # 木の回転によってヒープ性を保つ
        while (ptr.parent is not None) and (ptr.parent.priority > ptr.priority):
            if ptr.parent.right == ptr:
                self._rotate_left(ptr.parent)
            else:
                self._rotate_right(ptr.parent)
        if ptr.parent is None:
            self.root = ptr 
        return True

    def delete(self, val: int) -> True:
        """値の削除: 集合から値valを持つノードを削除する"""
        if self.root is None:
            return False

        ptr = self.root         
        while True: 
            if ptr is None:
                return False
            elif val < ptr.val:
                ptr = ptr.left
            elif val > ptr.val:
                ptr = ptr.right
            else:
                break

        # 木の回転によって削除したいノードを葉に持っていく
        while (ptr.left is not None) or (ptr.right is not None):
            if ptr.left is None:
                self._rotate_left(ptr)
            elif ptr.right is None:
                self._rotate_right(ptr)
            elif ptr.left.priority < ptr.right.priority:
                self._rotate_right(ptr)
            else:
                self._rotate_left(ptr)
            if self.root == ptr:
                self.root = ptr.parent

        # ノードの削除
        if ptr.left is None and ptr.right is None:
            if ptr == self.root:
                self.root = None
            elif ptr.parent.left == ptr:
                ptr.parent.left = None
            else:
                ptr.parent.right = None      
        return True

    def _rotate_left(self, ptr):
        """木の左回転を行う"""
        w = ptr.right
        w.parent = ptr.parent
        if w.parent is not None:
            if w.parent.left == ptr:
                w.parent.left = w
            else:
                w.parent.right = w
        ptr.right = w.left
        if ptr.right is not None:
            ptr.right.parent = ptr
        ptr.parent = w
        w.left = ptr
        if ptr == self.root:
            self.root = w
            self.root.parent = None

    def _rotate_right(self, ptr):
        """木の右回転を行う"""
        w = ptr.left
        w.parent = ptr.parent
        if w.parent is not None:
            if w.parent.right == ptr:
                w.parent.right = w
            else:
                w.parent.left = w
        ptr.left = w.right
        if ptr.left is not None:
            ptr.left.parent = ptr
        ptr.parent = w
        w.right = ptr
        if ptr == self.root:
            self.root = w
            self.root.parent = None

    def search_min(self):
        ptr = self.root
        ret = None
        while ptr is not None:
            ret = ptr.val
            ptr = ptr.left
        return ret

    def search_max(self):
        ptr = self.root
        ret = None
        while ptr is not None:
            ret = ptr.val
            ptr = ptr.right
        return ret

    def search_le(self, val: int):
        """val以下の最大の値を探す"""
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val <= val:
                ret = ptr.val
                ptr = ptr.right
            else:
                ptr = ptr.left
        return ret

    def search_lt(self, val: int):
        """valよりも小さいの最大の値を探す"""
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val < val:
                ret = ptr.val
                ptr = ptr.right
            else:
                ptr = ptr.left
        return ret

    def search_ge(self, val: int):
        """val以上の最小の値を探す"""
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val >= val:
                ret = ptr.val
                ptr = ptr.left
            else:
                ptr = ptr.right
        return ret
      
    def search_gt(self, val: int):
        """valよりも大きい最小の値を探す"""
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val > val:
                ret = ptr.val
                ptr = ptr.left
            else:
                ptr = ptr.right
        return ret
      
      
n = int(input())
s = list(map(int, input().split()))
s = sorted(s, reverse=True)

tp = Treap(is_multiset=True)
used = [False] * (1 << n)
tp.insert(s[0])
used[0] = True

for step in range(n):
    cnt = 1 << step
    res = []
    for i in range(1 << n):
        if used[i]:
            continue
        val = tp.search_gt(s[i])
        if val is not None:
            cnt -= 1
            res.append(val)
            res.append(s[i])
            tp.delete(val)
            used[i] = True
        if cnt == 0:
            for val in res:
                tp.insert(val)
            break
    else:
        print("No")
        exit()
print("Yes")