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
        return max(l + 1, r + 1)

def main():
    n = int(input().strip())
    nodes = [Node(i) for i in range(n)]

    ## get order
    preorder = [int(i)-1 for i in input().strip().split()] ## convert to 0-based index
    inorder = [int(i)-1 for i in input().strip().split()] ## convert to 0-based index

    def make_tree(preorder, inorder):
        if not preorder or not inorder:
            return None

        ## get root of tree
        root = nodes[preorder[0]]
        ## find divide point in inorder table
        idx = inorder.index(root.val)

        left_inorder = inorder[:idx]
        left_preorder = preorder[1:len(left_inorder)+1]
        right_inorder = inorder[idx + 1:]
        right_preorder = preorder[len(left_inorder) + 1:]

        ## create left and right tree
        root.left = make_tree(left_preorder,left_inorder)
        root.right = make_tree(right_preorder,right_inorder)

        return root

    make_tree(preorder, inorder)
    
    postorder = []

    def postorder_walk(node):
        if node.left:
            postorder_walk(node.left)
        if node.right:
            postorder_walk(node.right)
        postorder.append(str(node.val+1)) ## fix to 1-based index
    root = nodes[preorder[0]]
    postorder_walk(root)
    print(" ".join(postorder))


if __name__ == "__main__":
    main()
