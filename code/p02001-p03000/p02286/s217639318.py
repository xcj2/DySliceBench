NIL = -1


class Node():
    __slots__ = ["key", "parent", "left", "right"]

    def __init__(self, key=NIL):
        self.key = key
        self.parent = NIL
        self.left = NIL
        self.right = NIL

class NodeHeap(Node):
    __slots__ = ["priority"]

    def __init__(self,key=NIL, priority=NIL):
        super().__init__(key)
        self.priority = priority

class BinaryTree():
    def __init__(self):
        self.root = NIL

    def _isnil(self, x):
        if isinstance(x, int):
            return True
        else:
            return False

    def insert(self, key):
        if self.root == NIL:
            self.root = Node(key)
            return

        now = self.root
        while now != NIL:
            parent = now
            if   key < now.key:
                now = now.left
            elif key > now.key:
                now = now.right
            else:
                raise

        insert = self.get_newnode(key)
        insert.parent = parent

        if   insert.key < parent.key:
            parent.left = insert
        elif insert.key > parent.key:
            parent.right = insert
        else:
            raise

    def find(self, key):
        now = self.root
        while now != NIL and now.key != key:
            if   key < now.key:
                now = now.left
            elif key > now.key:
                now = now.right
            else:
                raise

        return now

    def delete(self, key):
        z = self.find(key)
        if self._isnil(z):
            return

        if z.left == NIL or z.right == NIL:
            y = z
        else:
            y = self.get_successor(z)

        if y.left != NIL:
            x = y.left
        else:
            x = y.right

        if x != NIL:
            x.parent = y.parent

        if y.parent == NIL:
            # delete:root
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y.key

    def get_successor(self, z):
        if z.right != NIL:
            return self.get_minimum(z.right)

        y = z.parent
        while y != NIL and z == y.right:
            z = y
            y = y.parent

        return y

    def get_minimum(self, x):
        while x.left != NIL:
            x = x.left

        return x

    def print_inorder(self):
        self._treewalk_inorder(self.root)
        print()

    def _treewalk_inorder(self, node):
        if self._isnil(node):
            return

        self._treewalk_inorder(node.left)
        print(f" {node.key}", end="")
        self._treewalk_inorder(node.right)

    def print_preorder(self):
        self._treewalk_preorder(self.root)
        print()

    def _treewalk_preorder(self, node):
        if self._isnil(node):
            return

        print(f" {node.key}", end="")
        self._treewalk_preorder(node.left)
        self._treewalk_preorder(node.right)

class Treap(BinaryTree):
    def __init__(self):
        self.root = NIL

    def _right_rotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s

    def _left_rotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def insert(self, key, priority):
        self.root = self._insert_main(self.root, key, priority)

    def _insert_main(self, node, key, priority):
        if node == NIL:
            return NodeHeap(key, priority)

        if   key > node.key:
            node.right = self._insert_main(node.right, key, priority)
            if node.priority < node.right.priority:
                node = self._left_rotate(node)
        elif key < node.key:
            node.left = self._insert_main(node.left, key, priority)
            if node.priority < node.left.priority:
                node = self._right_rotate(node)
        else:
            raise

        return node

    def delete(self, key):
        self.root = self._delete_main(self.root, key)

    def _delete_main(self, node, key):
        if node == NIL:
            return node

        if key < node.key:
            node.left = self._delete_main(node.left, key)
        elif key > node.key:
            node.right = self._delete_main(node.right, key)
        else:
            return self._delete_rotate(node, key)

        return node

    def _delete_rotate(self, node, key):
        if node.left == NIL and node.right == NIL:
            return NIL
        elif node.left == NIL:
            node = self._left_rotate(node)
        elif node.right == NIL:
            node = self._right_rotate(node)
        else:
            if node.left.priority > node.right.priority:
                node = self._right_rotate(node)
            else:
                node = self._left_rotate(node)

        return self._delete_main(node, key)


m = int(input())

treap = Treap()

for _ in range(m):

    command, *list_num = input().split()

    if   command == "insert":
        k = int(list_num[0])
        p = int(list_num[1])
        treap.insert(k, p)
    elif command == "find":
        k = int(list_num[0])
        if isinstance(treap.find(k), int):
            print("no")
        else:
            print("yes")
    elif command == "delete":
        k = int(list_num[0])
        treap.delete(k)
    elif command == "print":
        treap.print_inorder()
        treap.print_preorder()
    else:
        raise

