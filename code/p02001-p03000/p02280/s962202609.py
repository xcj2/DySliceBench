class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return "{ "+ str(self.parent) + " " + str(self.left) + " " + str(self.right) + " }"



class BinarySearchTree:
    def __init__(self,size):
        self.tree = [Node(-1,-1,-1) for i in range(size+1)]
        self.root = -1

    def add(self,key,right,left):
        self.tree[key].left = left
        self.tree[key].right = right
        self.tree[left].parent = key
        self.tree[right].parent = key 
        #print(self.tree)
        

    def calcHeight(self,next,sum):
        if next == -1:
            return sum -1
        return max(self.calcHeight(self.tree[next].left,sum+1),self.calcHeight(self.tree[next].right,sum+1))

    def calcDepth(self,next):
        #print("height",next)
        if next == -1:
            return -1
        return 1 + self.calcDepth(self.tree[next].parent)
    
    def getType(self,node):
        if node.parent == -1:
            return "root"
        elif node.right == node.left == -1:
            return "leaf"
        return "internal node"
    
    def printAll(self):
        for idx, node in enumerate(self.tree):
            if node.parent == -1:
                self.root = idx
                break
        self.tree.pop()
        for idx, node in enumerate(self.tree):
            parent = node.parent
            sibling = self.tree[node.parent].left
            if sibling == idx:
                sibling = self.tree[node.parent].right
            degree = 0
            if node.left != -1:
                degree += 1
            if node.right != -1:
                degree += 1
            depth = self.calcDepth(idx)
            height = self.calcHeight(idx,0)
            typed = self.getType(node)
            print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(idx,parent,sibling,degree, depth, height,typed))

N = int(input())
BST = BinarySearchTree(N)
for i in range(N):
    Q = list(map(int, input().split()))
    BST.add(Q[0],Q[1],Q[2])
BST.printAll()

            

