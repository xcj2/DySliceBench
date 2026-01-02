from random import random


class TreapNode():
    def __init__(self, val):
        self.val = val
        self.priority = random()
        self.parent = None
        self.right = None
        self.left = None
 
        
class Treap():
    def __init__(self, is_multiset=False):
        self.root = None
        self.is_multiset = is_multiset
 
    def search(self, val: int) -> bool:
        ptr = self.root
        while ptr is not None:
            if ptr.val == val:
                return True
            if val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False 
 
    def insert(self, val: int):
        if self.root is None:
            self.root = TreapNode(val)
            return
 
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
                    return
                if ptr.right is None:
                    ptr.right = TreapNode(val)
                    ptr.right.parent = ptr
                    ptr = ptr.right
                    break
                ptr = ptr.right
 
        while (ptr.parent is not None) and (ptr.parent.priority > ptr.priority):
            if ptr.parent.right == ptr:
                self.rotate_left(ptr.parent)
            else:
                self.rotate_right(ptr.parent)
        if ptr.parent is None:
            self.root = ptr 
       
    def delete(self, val: int):
        if self.root is None:
            return
 
        ptr = self.root         
        while True: 
            if ptr is None:
                return
            if ptr.val == val:
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
            elif ptr.left.priority < ptr.right.priority:
                self.rotate_right(ptr)
            else:
                self.rotate_left(ptr)
            if self.root == ptr:
                self.root = ptr.parent
       
        if ptr.left is None and ptr.right is None:
            if ptr == self.root:
                self.root = None
            elif ptr.parent.left == ptr:
                ptr.parent.left = None
            else:
                ptr.parent.right = None      
 
    def search_min(self, ptr):
        while True:
            if ptr.left is None:
                return ptr
            ptr = ptr.left
        return ptr
 
    def rotate_left(self, ptr):
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
 
    def search_less(self, val):
        if val == None:
            return None
        ptr = self.root
        ret = None
        while ptr is not None:
            if ptr.val < val:
                ret = ptr.val
                ptr = ptr.right
            else:
                ptr = ptr.left
        return ret


n = int(input())
a = list(map(int, input().split()))

tp = Treap(True)
max_a = max(a)

for i in range(2**n):
    tp.insert(a[i])

tp.delete(max_a)

slime = [max_a]
for _ in range(n):
    li = []
    for val in slime:
        tmp = tp.search_less(val)
        if tmp is None:
            print("No")
            exit()
        tp.delete(tmp)
        li.append(tmp)
    slime = slime + li
print("Yes")