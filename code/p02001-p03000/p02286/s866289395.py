class Node:
    def __init__(self,key,priority,left=None,right=None):
        self.left = left
        self.right = right
        self.key = key
        self.priority = priority

def insert(t,key,priority):
    if t == None :
        return Node(key,priority)
    if key == t.key :
        return t
    if key < t.key :
        t.left = insert(t.left, key, priority)
        if t.priority < t.left.priority :
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, priority)
        if t.priority < t.right.priority :
            t = leftRotate(t)
    return t


def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s


def leftRotate(t):
    s= t.right
    t.right = s.left
    s.left = t
    return s


def find(t,key):
    if t == None: return None
    elif t.key == key:return t
    elif t.key > key :return find(t.left,key)
    else: return find(t.right,key)

def erase(t, key):
    if t == None : return None
    if key == t.key:
        if t.left == None and t.right == None:return None
        elif t.left == None : t = leftRotate(t)
        elif t.right == None : t = rightRotate(t)
        else:
            if t.left.priority > t.right.priority:t = rightRotate(t)
            else: t = leftRotate(t)
        return erase(t, key)
    elif key < t.key : t.left = erase(t.left, key)
    else : t.right = erase(t.right, key)
    return t

def inorder(t):
    if t.left != None:inorder(t.left)
    print(" "+str(t.key), end='')
    if t.right != None: inorder(t.right)

def preorder(t):
    print(" "+str(t.key), end='')
    if t.left != None :preorder(t.left)
    if t.right != None : preorder(t.right)

if __name__=="__main__":
        m=(int)(input())
        root = None
        for i in range(m):
            order = input().split()
            if order[0] == "insert" :root = insert(root,(int)(order[1]),(int)(order[2]))
            elif order[0] == "delete" :root = erase(root,(int)(order[1]))
            elif order[0] == "find" :
                res = find(root,(int)(order[1]))
                if res == None :print("no")
                else:print("yes")
            else:
                inorder(root)
                print()
                preorder(root)
                print()

