from functools import reduce
from collections import namedtuple
Node = namedtuple('Node', ['parent', 'children'])
 
class my_binary_tree:
    def __init__(self, N=[]):
        self.T = {}
        for ni in N: self.addNode(ni)
 
    def addNode(self, n):
        p = self.T.get(n[0],Node(-1,[-1,-1])).parent
        self.T[n[0]] = Node(p,n[1:])
        for c in n[1:]:
            if c > -1:  
                cc = self.T.get(c,Node(-1,[-1,-1])).children
                self.T[c] = Node(n[0],cc)
 
    def getParent(self, i): return self.T[i].parent
 
    def getChildren(self, i): return self.T[i].children
 
    def getDepth(self, i):
        if self.T[i].parent == -1: return 0
        return self.getDepth(self.T[i].parent) + 1
 
    def getHeight(self, i):
        c0 = self.T[i].children[0]
        c1 = self.T[i].children[1]
        if c0 + c1 == -2: return 0
        return max( ( 0 if c0 == -1 else self.getHeight(c0) ), \
                    ( 0 if c1 == -1 else self.getHeight(c1) ) )\
               + 1
 
    def getDegree(self, i):
        return int(self.T[i].children[0] != -1) + \
               int(self.T[i].children[1] != -1)
 
    def getNodeType(self, i):
        if self.T[i].parent == -1        : return 'root'
        if sum(self.T[i].children) == -2 : return 'leaf'
        return 'internal node'
 
    def getSibling(self, i):
        p = self.T[i].parent
        if p == -1: return -1
        return sum(self.T[p].children) - i
 
    def getIdList(self): return sorted(self.T.keys())
 
  
if __name__=='__main__':
    n = int(input())
    N = [None]*n
    for i in range(n): N[i] = list(map(int,input().split()))
    tree = my_binary_tree(N)
      
    for i in tree.getIdList():        
        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(\
                i, tree.getParent(i), tree.getSibling(i), tree.getDegree(i), tree.getDepth(i), tree.getHeight(i), tree.getNodeType(i)))