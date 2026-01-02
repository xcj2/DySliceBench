class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        x = TreeNode(v)
        if not self.root:
            self.root = x
            return

        r = self.root
        while r is not None:
            parent = r
            if x.val < r.val:
                r = r.left
            else:
                r = r.right

        if x.val < parent.val:
            parent.left = x
        else:
            parent.right = x

    def in_order(self):
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        res = []
        helper(self.root)
        return res

    def pre_order(self):
        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)

        res = []
        helper(self.root)
        return res

    def find(self, target):
        if not self.root:
            return False
        r = self.root
        while r:
            if target < r.val:
                r = r.left
            elif target == r.val:
                return True
            else:
                r = r.right
        return False


test = BST()
n = int(input())
for _ in range(n):
    order = input()
    if order.startswith("insert"):
        i, x = order.split()
        test.insert(int(x))
    elif order.startswith("find"):
        i, x = order.split()
        print("yes" if test.find(int(x)) else "no")
    else:
        print(" ",end="")
        print(*test.in_order())
        print(" ",end="")
        print(*test.pre_order())

