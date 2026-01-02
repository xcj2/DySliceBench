from collections import namedtuple
Node = namedtuple('Node', ['parent', 'children'])

class my_tree:
    def __init__(self, N=[]):
        self.T = {}
        for ni in N: self.addNode(ni)

    def addNode(self, n):
        p = self.T.get(n[0],Node(-1,[None])).parent
        self.T[n[0]] = Node(p,n[2:])
        for c in n[2:]:
            cc = self.T.get(c,Node(-1,[None])).children
            self.T[c] = Node(n[0],cc)

    def getParent(self, i): return self.T[i].parent

    def getChildren(self, i): return self.T[i].children

    def getDepth(self, i):
        if self.T[i].parent == -1: return 0
        return self.getDepth(self.T[i].parent) + 1

    def getNodeType(self, i):
        if self.T[i].parent == -1: return 'root'
        if self.T[i].children    : return 'internal node'
        return 'leaf'

    def getIdList(self): return sorted(self.T.keys())

 
if __name__=='__main__':
    n = int(input())
    N = [None]*n
    for i in range(n): N[i] = list(map(int,input().split()))
    tree = my_tree(N)
     
    for i in tree.getIdList():        
        print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(\
                i, tree.getParent(i), tree.getDepth(i), tree.getNodeType(i), tree.getChildren(i)))