class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = self.right = None
    def nextNode(self):
        if not self.right:
            return None
        x = self.right
        while x.left:
            x = x.left
        return x
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

def find(t, k):
    x = t
    while x:
        if x.key == k:
            return x
        x = x.left if k < x.key else x.right
    return None

def delete(t, k):
    node = find(t, k)
    delNode(node)

def delNode(node):
    if not node: return
    if not node.left and not node.right: # 子がないとき
        if node == node.parent.left:
            node.parent.left = None
        if node == node.parent.right:
            node.parent.right = None
    elif not node.right: # 左の子だけのとき
        if node == node.parent.left:
            node.parent.left = node.left
        if node == node.parent.right:
            node.parent.right = node.left
        node.left.parent = node.parent
    elif not node.left: # 右の子だけのとき
        if node == node.parent.left:
            node.parent.left = node.right
        if node == node.parent.right:
            node.parent.right = node.right
        node.right.parent = node.parent
    else: # 子が２つのとき
        next = node.nextNode()
        node.key = next.key
        delNode(next)

t = None
m = int(input())
for _ in range(m):
    cmd = list(input().split())
    if cmd[0] == 'insert':
        t = insert(t, Node(int(cmd[1])))
    if cmd[0] == 'find':
        print('yes' if find(t, int(cmd[1])) else 'no')
    if cmd[0] == 'delete':
        delete(t, int(cmd[1]))
    if cmd[0] == 'print':
        print('', *t.inorder())
        print('', *t.preorder())

