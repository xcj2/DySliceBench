class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
class Treap:
    def __init__(self):
        self.root = None
        self.order_list = []
    def right_rotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s
    def left_rotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s
    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None
    def insert(self, t, key, priority):
        if t == None:
            return Node(key, priority)
        if key == t.key:
            return t
        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if priority > t.priority:
                t = self.right_rotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if priority > t.priority:
                t = self.left_rotate(t)
        return t
    def delete(self, t, key):
        if t == None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self.__delete(t, key)
        return t
    def __delete(self, t, key):
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = self.left_rotate(t)
        elif t.right == None:
            t = self.right_rotate(t)
        else:
            if t.left.priority < t.right.priority:
                t = self.left_rotate(t)
            else:
                t = self.right_rotate(t)
        return self.delete(t, key)
    def walk_preorder(self, node):
        if node == None:
            return None
        self.order_list.append(node.key)
        self.walk_preorder(node.left)
        self.walk_preorder(node.right)
    def walk_inorder(self, node):
        if node == None:
            return None
        self.walk_inorder(node.left)
        self.order_list.append(node.key)
        self.walk_inorder(node.right)
    def print_nodes(self):
        self.order_list = []
        self.walk_inorder(self.root)
        inorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(inorder_str))
        self.order_list = []
        self.walk_preorder(self.root)
        preorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(preorder_str))
n = int(input())
tree = Treap()
for _ in range(n):
    command = input().split(' ')
    if len(command) == 1:
        tree.print_nodes()
    elif len(command) == 2:
        opecode, key = command[0], int(command[1])
        if opecode == 'delete':
            tree.root = tree.delete(tree.root, key)
        elif opecode == 'find':
            if tree.find(key) != None:
                print('yes')
            else:
                print('no')
    else:
        opecode, key, priority = command[0], int(command[1]), int(command[2])
        tree.root = tree.insert(tree.root, key, priority)
