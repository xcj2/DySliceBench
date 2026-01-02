class Node:
    def __init__(self, key, priority, left=None, right=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right


def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s # 部分木の新しい根を返す


def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s # 部分木の新しい根を返す


def insert(t, key, priority):
    # 葉に到達したらノードを生成して返す
    if t == None:
        return Node(key, priority)
    # 重複するキーを無視する
    if key == t.key:
        return t

    if key < t.key: # 左の子に移動
        # 帰ってきたノードを左の子にする
        t.left = insert(t.left, key, priority)
        # その子に優先度が高ければ、右回転で持ち上げる
        if t.priority < t.left.priority:
            t = rightRotate(t)
    else: # 右の子に移動
        # 帰ってきたノードを右の子にする
        t.right = insert(t.right, key, priority)
        # その子の優先度が高ければ左回転で持ち上げる
        if t.priority < t.right.priority:
            t = leftRotate(t)

    return t


def erase(t, key):
    if t == None:
        return None

    if key == t.key: # tが削除対象
        if (t.left == None) and (t.right == None): # tが葉
            return None
        elif t.left == None: # tがただ一つの右の子を持つ
            t = leftRotate(t)
        elif t.right == None:
            t = rightRotate(t) # tがただ一つの左の子を持つ
        else: # tが二つの子を持つ
            # 優先度が高い子を持ち上げる
            if t.left.priority > t.right.priority:
                t = rightRotate(t)
            else:
                t = leftRotate(t)
        return erase(t, key)

    # 対象を再帰的に探索
    elif key > t.key:
        t.right = erase(t.right, key)
    else:
        t.left = erase(t.left, key)
    return t


# 引数のkeyを持つノードの有無を探索
def find(t, key):
    if t.key == key:
        print("yes")
    elif t.key < key and t.right != None:
        find(t.right, key)
    elif t.key > key and t.left != None:
        find(t.left, key)
    else:
        print("no")
    return 0


def in_print(t):
    if t.left != None:
        in_print(t.left)
    print(" " + str(t.key), end='')
    if t.right != None:
        in_print(t.right)

# 中間巡回アルゴリズム
def pre_print(t):
    print(" " + str(t.key), end='')
    if t.left != None:
        pre_print(t.left)
    if t.right != None:
        pre_print(t.right)


def main():
    Treap = None
    p = []
    k = int(input())
    i = 0
    while i < k:
        try:
            p.append(list(map(str, input().split())))
            i = i + 1
        except:
            break;
    
    i = 0
    while i < k:
        if p[i][0] == 'insert':
            key = int(p[i][1])
            priority = int(p[i][2])
            Treap = insert(Treap, key, priority)
        elif p[i][0] == 'find':
            key = int(p[i][1])
            find(Treap, key)
        elif p[i][0] == 'delete':
            key = int(p[i][1])
            Treap = erase(Treap, key)
        else:
            in_print(Treap)
            print()
            pre_print(Treap)
            print()
        i = i + 1

if __name__ == '__main__':
    main()
