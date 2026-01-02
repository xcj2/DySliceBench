import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.depth = 0
    
    def get_depth(self):
        if not self.parent:
            return 0
        else:
            return self.parent.get_depth()+1
    
    def get_sibling(self):
        if not self.parent:
            return - 1
        else:
            if self.parent.right and self.parent.right.val == self.val:
                if self.parent.left:
                    return self.parent.left.val
                else:
                    return - 1
            elif self.parent.left and self.parent.left.val == self.val:
                if self.parent.right:
                    return self.parent.right.val
                else:
                    return - 1
    
    def get_parent(self):
        if not self.parent:
            return -1
        return self.parent.val
    
    def get_degree(self):
        degree = 0
        if self.left:
            degree += 1
        if self.right:
            degree += 1
        return degree
    
    def get_type(self):
        if not self.parent:
            return "root"
        elif self.left or self.right:
            return "internal node"
        else:
            return "leaf"
    
    def get_height(self):
        if not self.left and not self.right:
            return 0
        l,r = 0,0
        if self.left:
            l = self.left.get_height()
        if self.right:
            r = self.right.get_height()
        return max(l + 1,r + 1)


def main():
    n = int(input().strip())
    nodes = [Node(i) for i in range(n)]

    ## create binary tree
    for _ in range(n):
        val, left, right = [int(i) for i in input().strip().split()]
        if left != -1:
            nodes[val].left,nodes[left].parent = nodes[left],nodes[val]
        if right != -1:
            nodes[val].right,nodes[right].parent = nodes[right],nodes[val]

    ## find root node
    depth = [node.get_depth() for node in nodes]
    root = nodes[depth.index(0)]

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

    ## postorder walk

    postorder = []

    def postorder_walk(node):
        if node.left:
            postorder_walk(node.left)
        if node.right:
            postorder_walk(node.right)
        postorder.append(str(node.val))

    preorder_walk(root)
    inorder_walk(root)
    postorder_walk(root)

    print("Preorder")
    print(""," ".join(preorder))
    print("Inorder")
    print(""," ".join(inorder))
    print("Postorder")
    print(""," ".join(postorder))


if __name__ == "__main__":
    main()
