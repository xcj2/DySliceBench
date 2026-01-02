n = int(input())
NIL = -1
MAX = 10000

class Node():
    def __init__(self):
        self.parent = [0] * MAX
        self.left = [0] * MAX
        self.right = [0] * MAX
        self.Pr = []
        self.I = []
        self.Po = []
        
    def preparse(self, u):
        if u == NIL:
            return
        self.Pr.append(u)
        self.preparse(self.left[u])
        self.preparse(self.right[u])
        return self
    
    def inoparse(self, u):
        if u == NIL:
            return
        self.inoparse(self.left[u])
        self.I.append(u)
        self.inoparse(self.right[u])
        return self
    
    def postparse(self, u):
        if u == NIL:
            return
        self.postparse(self.left[u])
        self.postparse(self.right[u])
        self.Po.append(u)
        return self
        
def main():
    T = Node()
    for i in range(n):
        T.parent[i] = NIL
    
    for i in range(n):
        v, l, r = (int(x) for x in input().split())
        T.left[v] = l
        T.right[v] = r
        if l != NIL:
            T.parent[l] = v
        if r != NIL:
            T.parent[r] = v
    
    for i in range(n):
        if T.parent[i] == NIL:
            root = i
    
    T.preparse(root)
    T.inoparse(root)
    T.postparse(root)
    pr = [str(i) for i in T.Pr]
    ino = [str(i) for i in T.I]
    po = [str(i) for i in T.Po]
    
    print('Preorder')
    print(' ' + ' '.join(pr))
    print('Inorder')
    print(' ' + ' '.join(ino))
    print('Postorder')
    print(' ' + ' '.join(po))

main()
