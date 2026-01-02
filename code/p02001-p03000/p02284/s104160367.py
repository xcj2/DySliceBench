###
# 二分探索木2
###

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, node: Node):
        self.count += 1
        if not self.root:
            self.root = node
            return

        cur = self.root
        while cur:
            if node.val > cur.val:
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    cur.right,node.parent = node,cur
                    return
            else:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left,node.parent = node,cur
                    return

    def find(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return "yes"
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return "no"


def main():

    ## preorder tree walk
    preorder = []

    def preorder_walk(node):
        preorder.append(str(node.val))
        if node.left:
            preorder_walk(node.left)
        if node.right:
            preorder_walk(node.right)

    ## inorder tree walk

    inorder = []

    def inorder_walk(node):
        if node.left:
            inorder_walk(node.left)
        inorder.append(str(node.val))
        if node.right:
            inorder_walk(node.right)


    n = int(input())
    
    bst = BinarySearchTree()
    
    for _ in range(n):
        op = input().strip().split()
        if op[0] == "insert":
            bst.insert(Node(int(op[1])))
        elif op[0] == "print":
            preorder,inorder = [],[]
            preorder_walk(bst.root)
            inorder_walk(bst.root)
            print(""," ".join(inorder))
            print("", " ".join(preorder))
        elif op[0] == "find":
            print(bst.find(int(op[1])))

if __name__ == "__main__":
    main()

