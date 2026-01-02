class Node:
    def __init__(self, key:int, priority:int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def leftRotate(self, t:Node):
        s:Node = t.right
        t.right = s.left
        s.left = t
        if t.key == self.root.key:
            self.root = s
        return s

    def rightRotate(self, t:Node):
        s:Node = t.left
        t.left = s.right
        s.right = t
        if t.key == self.root.key:
            self.root = s        
        return s

    def insert(self, t:Node, key:int, priority:int):
        if not self.root:
            self.root = Node(key, priority)
            return self.root
        if not t:
            return Node(key, priority)
        if key == t.key:
            return t
        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.leftRotate(t)
        return t

    def delete(self, t:Node, key:int):
        if not t:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self._delete(t, key)
        return t

    def _delete(self, t:Node, key:int):
        if not t.left and not t.right:
            return None
        elif not t.left:
            t = self.leftRotate(t)
        elif not t.right:
            t = self.rightRotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self.delete(t, key)


def Preorder(target:Node):
    yield target.key
    if target.left != None:
        yield from Preorder(target.left)
    if target.right != None:
        yield from Preorder(target.right)

def Inorder(target:Node):
    if target.left != None:
        yield from Inorder(target.left)
    yield target.key
    if target.right != None:
        yield from Inorder(target.right)

def find(target:Node,findkey:int):
    return node_of_key(target, findkey) != None

def node_of_key(target:Node,findkey:int):
    if target.key == findkey:
        return target
    elif target.key > findkey:
        if target.left:
            return node_of_key(target.left, findkey)
    else:
        if target.right:
            return node_of_key(target.right, findkey)
    return None

def min_value_node_of_tree(root:Node):
    if root.left == None:
        return root
    else:
        return min_value_node_of_tree(root.left)


from sys import stdin
tree = Tree()
n = int(input())
lines = stdin.readlines()
for line in lines:
    proc,*param = line.split()
    if proc == "insert":
        if not tree.root:
            tree.root = Node(int(param[0]), int(param[1]))
        else:
            tree.insert(tree.root, int(param[0]), int(param[1]))
    elif proc == "find":
        print("yes" if find(tree.root, int(param[0])) else "no")
    elif proc == "delete":
        tree.delete(tree.root, int(param[0]))
    else:
        print(" ",end="")
        print(*Inorder(tree.root))
        print(" ",end="")
        print(*Preorder(tree.root))
