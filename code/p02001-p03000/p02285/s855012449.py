class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            parent = None
            cur = self.root
            while cur:
                parent = cur
                if val < cur.val:
                    cur = cur.left
                elif cur.val < val:
                    cur = cur.right

            if val < parent.val:
                parent.left = TreeNode(val)
            elif parent.val < val:
                parent.right = TreeNode(val)

    def find(self, val):
        if not self.root:
            return False
        else:
            cur = self.root
            while cur:
                if val < cur.val:
                    cur = cur.left
                elif cur.val < val:
                    cur = cur.right
                else:
                    return True
            return False

    def remove(self, val):
        self._remove(self.root, val, None)

    def _remove(self, node, val, parent):
        if not node:
            return
        elif val < node.val:
            self._remove(node.left, val, node)
        elif node.val < val:
            self._remove(node.right, val, node)
        else:
            if node.left and node.right:
                # Find min value from right sub-tree
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.val = cur.val
                self._remove(node.right, cur.val, node)
            elif node.left:
                if parent.left == node:
                    parent.left = node.left
                elif parent.right == node:
                    parent.right = node.left
            elif node.right:
                if parent.left == node:
                    parent.left = node.right
                elif parent.right == node:
                    parent.right = node.right
            else:
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None


def inorder(node):
    if node:
        res = []
        res += inorder(node.left)
        res.append(node.val)
        res += inorder(node.right)
        return res
    else:
        return []


def preorder(node):
    if node:
        res = [node.val]
        res += preorder(node.left)
        res += preorder(node.right)
        return res
    else:
        return []


if __name__ == '__main__':
    n = int(input())
    bst = BinarySearchTree()
    for _ in range(n):
        cmd, *num = input().split()
        if cmd == 'insert':
            bst.insert(int(num[0]))
        elif cmd == 'find':
            if bst.find(int(num[0])):
                print('yes')
            else:
                print('no')
        elif cmd == 'delete':
            bst.remove(int(num[0]))
        else:
            for x in inorder(bst.root):
                print(f' {x}', end='')
            print()
            for x in preorder(bst.root):
                print(f' {x}', end='')
            print()
