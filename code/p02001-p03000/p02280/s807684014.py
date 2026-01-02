###
# 二分木
###

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
    for _ in range(n):
        val, left, right = [int(i) for i in input().strip().split()]
        if left != -1:
            nodes[val].left,nodes[left].parent = nodes[left],nodes[val]
        if right != -1:
            nodes[val].right,nodes[right].parent = nodes[right],nodes[val]

    for id in range(n):
        p = nodes[id].get_parent()
        s = nodes[id].get_sibling()
        deg = nodes[id].get_degree()
        dep = nodes[id].get_depth()
        h = nodes[id].get_height()
        _type = nodes[id].get_type()
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(id, p, s, deg, dep, h, _type))


if __name__ == "__main__":
    main()
