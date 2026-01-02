from random import random


class TreapNode():
    """Treapが保持するノードを定義する。
    ノードは値と優先度、および親と子へのポインタを持つ。"""
    def __init__(self, val):
        self.val = val
        self.priority = random()
        self.parent, self.right, self.left = None, None, None

class Treap():
    def __init__(self, multiset=True):
        self.root = None

    def search(self, val: int) -> bool:
        """集合に値valを持つノードが存在するかどうかを返す。"""
        ptr = self.root
        while ptr is not None:
            if ptr.val == val:
                return True
            if val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False

    def insert(self, val: int) -> bool:
        """集合に値valを持つノードを挿入する。
        挿入に成功したときTrue、失敗したときにFalseを返す。"""
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
                if ptr.right is None:
                    ptr.right = TreapNode(val)
                    ptr.right.parent = ptr
                    ptr = ptr.right
                    break
                ptr = ptr.right

        # 木の回転によりヒープ性を保つ
        while (ptr.parent is not None) and (ptr.parent.priority > ptr.priority):
            if ptr.parent.right == ptr:
                self.rotate_left(ptr.parent)
            else:
                self.rotate_right(ptr.parent)
        if ptr.parent is None:
            self.root = ptr 
        return True

    def delete(self, val: int) -> True:
        """集合から値valを持つノードを削除する。
        削除に成功したときTrue、失敗したときにFalseを返す。"""
        if self.root is None:
            return False

        ptr = self.root         
        while True: 
            if ptr is None:
                return False
            if ptr.val == val:
                break
            elif val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right

        # 木の回転により削除したいノードを葉に持っていく
        while (ptr.left is not None) or (ptr.right is not None):
            if ptr.left is None:
                self.rotate_left(ptr)
            elif ptr.right is None:
                self.rotate_right(ptr)
            elif ptr.left.priority < ptr.right.priority:
                self.rotate_right(ptr)
            else:
                self.rotate_left(ptr)
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

    def rotate_left(self, ptr):
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

    def rotate_right(self, ptr):
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

    def search_less_than(self, val):
        if val == None:
            return None
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val >= val:
                ptr = ptr.left
            else:
                ret = ptr.val
                ptr = ptr.right
        return ret

n = int(input())
a = [int(input()) for i in range(n)]
tp = Treap()
cnt = 0
for i in range(n):
    num = tp.search_less_than(a[i])
    if num is None:
        tp.insert(a[i])
        cnt += 1
    else:
        tp.delete(num)
        tp.insert(a[i])
print(cnt)