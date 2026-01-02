import random
from collections import deque


class TreapNode():
    """節クラス: valは節の値, priorityは節の優先度を表す
    parent/left/rightはそれぞれ親/左側の子/右側の子へのポインタを表す
    """
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority # random.random()
        self.parent = None
        self.right = None
        self.left = None


class Treap():
    """SSet(Sorted Set)をサポートする"""
    def __init__(self):
        self.root = None

    def search(self, val: int) -> bool:
        """二分木に値valを持つ節が存在するかどうか判定する
        valと一致する節が存在する場合はTrue、存在しない場合はFalseを返す
        """
        ptr = self.root
        while ptr is not None:
            if ptr.val == val:
                return True
            if val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False 

    def insert(self, val: int, priority):
        """二分木に値valを持つ節が存在しない場合、追加する"""
        if self.root is None:
            self.root = TreapNode(val, priority)
            return

        ptr = self.root 
        while True:
            if val == ptr.val:
                return
            elif val < ptr.val:
                if ptr.left is None:
                    # ポインタの示す先に節が存在しない場合はNode(val)を追加する
                    ptr.left = TreapNode(val, priority)
                    ptr.left.parent = ptr
                    ptr = ptr.left
                    break
                ptr = ptr.left
            else:
                if ptr.right is None:
                    # ポインタの示す先に節が存在しない場合はNode(val)を追加する
                    ptr.right = TreapNode(val, priority)
                    ptr.right.parent = ptr
                    ptr = ptr.right
                    break
                ptr = ptr.right
       
        while (ptr.parent is not None) and (ptr.parent.priority < ptr.priority):
            if ptr.parent.right == ptr:
                self.rotate_left(ptr.parent)
            else:
                self.rotate_right(ptr.parent)
        if ptr.parent is None:
            self.root = ptr 
          
          
    def delete(self, val: int):
        """二分木から値valを持つ節を削除する"""        
        ptr = self.root             
        while True: 
            if ptr is None:
                return
            elif val == ptr.val:
                break
            elif val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
       
        while (ptr.left is not None) or (ptr.right is not None):
            if ptr.left is None:
                self.rotate_left(ptr)
            elif ptr.right is None:
                self.rotate_right(ptr)
            elif ptr.left.priority > ptr.right.priority:
                self.rotate_right(ptr)
            else:
                self.rotate_left(ptr)
            if self.root == ptr:
                self.root = ptr.parent
       
        if ptr.parent.left == ptr:
            ptr.parent.left = None
        else:
            ptr.parent.right = None         
   
    def rotate_left(self, ptr):
        """木を左回転する"""
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
        """木を右回転する"""
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

    def preorder_tree_walk(self):
        """先行順巡回(preorder tree walk)"""
        res = []
        q = deque([])
        ptr = self.root
        while True:
            if ptr is not None:
                q.append(ptr) 
                res.append(ptr.val)
                ptr = ptr.left
            elif q: 
                ptr = q.pop() 
                ptr = ptr.right
            else:
                return res
 
    def inorder_tree_walk(self):
        """中間順巡回(inorder tree walk)"""
        res = []
        q = deque([])
        ptr = self.root
        while True:
            if ptr is not None:
                q.append(ptr) 
                ptr = ptr.left
            elif q: 
                ptr = q.pop() 
                res.append(ptr.val)
                ptr = ptr.right
            else:
                return res
 
    def postorder_tree_walk(self):
        """後行順巡回(postorder tree walk)"""
        res = []
        q = deque([self.root])
        ptr = self.root
        while q:
            ptr = q.pop()
            res.append(ptr.val)
            if ptr.left is not None:
                q.append(ptr.left)
            if ptr.right is not None:
                q.append(ptr.right)
        return reversed(res)

n = int(input())
info = [list(input().split()) for i in range(n)]
tp = Treap()

for i in range(n):
    if info[i][0] == "insert":
        tp.insert(int(info[i][1]), int(info[i][2]))
    elif info[i][0] == "find":
        if tp.search(int(info[i][1])):
            print("yes")
        else:
            print("no")
    elif info[i][0] == "delete":
        tp.delete(int(info[i][1]))
    else:
        print(" ", end="")
        print(*tp.inorder_tree_walk())
        print(" ", end="")
        print(*tp.preorder_tree_walk())
