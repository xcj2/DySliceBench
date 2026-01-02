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



n = int(input())

root = Node()
binary_tree = BinaryTree(root)


for _ in range(n):

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
    elif command == "print":
        binary_tree.treewalk_inorder(root)
        print()
        binary_tree.treewalk_preorder(root)
        print()
    else:
        raise

