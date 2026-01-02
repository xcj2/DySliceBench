NIL = -1


class Node():
    __slots__ = ["key", "parent", "left", "right"]

    def __init__(self, key=NIL, parent=NIL, left=NIL, right=NIL):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, node):
        self.root = node

    def insert(self, key):
        if self.root.key == NIL:
            self.root.key = key
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
        
        insert = Node(key, parent)

        if   insert.key < parent.key:
            parent.left = insert
        elif insert.key > parent.key:
            parent.right = insert
        else:
            raise

    def find(self, key):
        now = self.root
        while now != NIL:
            if   key < now.key:
                now = now.left
            elif key > now.key:
                now = now.right
            else:
                break

        return now

    def delete(self, key):
        z = self.find(key)
        if isinstance(z, int):
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
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y.key

    def get_successor(self, x):
        if x.right != NIL:
            return self.get_minimum(x.right)

        y = x.parent
        while y != NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def get_minimum(self, x):
        while x.left != NIL:
            x = x.left

        return x

    def treewalk_inorder(self, node):
        if isinstance(node, int):
            return

        self.treewalk_inorder(node.left)
        print(f" {node.key}", end="")
        self.treewalk_inorder(node.right)

    def treewalk_preorder(self, node):
        if isinstance(node, int):
            return

        print(f" {node.key}", end="")
        self.treewalk_preorder(node.left)
        self.treewalk_preorder(node.right)



m = int(input())

root = Node()
binary_tree = BinaryTree(root)


for _ in range(m):

    command, *list_num = input().split()

    if   command == "insert":
        k = int(list_num[0])
        binary_tree.insert(k)
    elif command == "find":
        k = int(list_num[0])
        if isinstance(binary_tree.find(k), int):
            print("no")
        else:
            print("yes")
    elif command == "delete":
        k = int(list_num[0])
        binary_tree.delete(k)
    elif command == "print":
        binary_tree.treewalk_inorder(root)
        print()
        binary_tree.treewalk_preorder(root)
        print()
    else:
        raise
