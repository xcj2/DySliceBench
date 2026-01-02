class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = self.right = None
    def preorder(self):
        L = [self.key]
        if self.left: L += self.left.preorder()
        if self.right: L += self.right.preorder()
        return L
    def inorder(self):
        L = []
        if self.left: L += self.left.inorder()
        L.append(self.key)
        if self.right: L += self.right.inorder()
        return L

def insert(t, z):
    y = None
    x = t
    while x:
        y = x # 親を設定
        x = x.left if z.key < x.key else x.right
    z.parent = y
    if not y: # t が空の場合
        return z
    if z.key < y.key:
        y.left = z # z を y の左の子にする
    else:
        y.right = z # z を y の右の子にする
    return t

t = None
m = int(input())
for _ in range(m):
    cmd = list(input().split())
    if cmd[0] == 'insert':
        t = insert(t, Node(int(cmd[1])))
    if cmd[0] == 'print':
        print('', *t.inorder())
        print('', *t.preorder())

