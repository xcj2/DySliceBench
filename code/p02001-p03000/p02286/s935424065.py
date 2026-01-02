class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
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

def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s # root of the subtree
def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s # root of the subtree

def insert(t, key, priority):
    if not t:
        return Node(key, priority) # 葉に到達したら新しい節点を生成して返す
    if key == t.key:
        return t # 重複したkeyは無視
    if key < t.key: # 左の子に移動
        t.left = insert(t.left, key, priority) # 左の子へのポインタを更新
        if t.priority < t.left.priority: # 左の子の方が優先度が高い場合右回転
            t = rightRotate(t)
    else: # 右の子へ移動
        t.right = insert(t.right, key, priority) # 右の子へのポインタを更新
        if t.priority < t.right.priority: # 右の子の方が優先度が高い場合左回転
            t = leftRotate(t)
    return t

def delete(t, key):
    if not t:
        return None
    if key < t.key: # 削除対象を検索
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    return t
def _delete(t, key):
    if not t.left and not t.right: # 葉の場合
        return None
    if not t.left: # 右の子のみを持つ場合左回転
        t = leftRotate(t)
    elif not t.right: # 左の子のみを持つ場合右回転
        t = rightRotate(t)
    else: # 左の子と右の子を両方持つ場合、優先度が高い方を持ち上げる
        if t.left.priority > t.right.priority:
            t = rightRotate(t)
        else:
            t = leftRotate(t)
    return delete(t, key)

def find(t, k):
    x = t
    while x:
        if x.key == k:
            return x
        x = x.left if k < x.key else x.right
    return None

t = None
m = int(input())
for _ in range(m):
    cmd = list(input().split())
    if cmd[0] == 'insert':
        t = insert(t, int(cmd[1]), int(cmd[2]))
    if cmd[0] == 'find':
        print('yes' if find(t, int(cmd[1])) else 'no')
    if cmd[0] == 'delete':
        t = delete(t, int(cmd[1]))
    if cmd[0] == 'print':
        print('', *t.inorder())
        print('', *t.preorder())

