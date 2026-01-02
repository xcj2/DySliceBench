class Node():
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def is_root(self):
        return self.parent is None

    def num_children(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_parent(self):
        return self.parent is not None

    def __key(self, obj):
        if isinstance(obj, int):
            return obj
        if isinstance(obj, Node):
            return obj.key

class Tree():
    def __init__(self, num_list=[]):
        self.root = None
        for num in num_list:
            self.insert(num)

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        parent = None
        target = self.root
        while target is not None:
            parent = target
            if key < target.key:
                target = target.left
            else:
                target = target.right
        node = Node(key, parent)
        if node.is_root():
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def find(self, key):
        if self.is_empty():
            return None
        else:
            node = self.root
            while node is not None:
                if key == node.key:
                    return node
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right
            return node

    def __preorder(self, node):
        if node is None:
            return []
        return [node.key] + self.__preorder(node.left) + self.__preorder(node.right)

    def __inorder(self, node):
        if node is None:
            return []
        return self.__inorder(node.left) + [node.key] + self.__inorder(node.right)

    def __postorder(self, node):
        if node is None:
            return []
        return self.__postorder(node.left) + self.__postorder(node.right) + [node.key]

    def preorder(self):
        return self.__preorder(self.root)

    def inorder(self):
        return self.__inorder(self.root)

    def postorder(self):
        return self.__postorder(self.root)

    def get_minimum(self, node):
        target = node
        while target.has_left():
            target = target.left
        return target

    def get_successor(self, node):
        target = node
        if target.has_right():
            return self.get_minimum(target.right)
        else:
            while target.has_parent():
                if target.parent.left is target:
                    return target.parent
                target = target.parent
            return None

    def delete(self, key):
        node = self.find(key)
        if node is None:
            raise ValueError
        if node.num_children() == 2:
            denode = self.get_successor(node)
        else:
            denode = node
        # denodeは片方にしかない
        if denode.has_left():
            child = denode.left
        else:
            child = denode.right

        # denodeの下から上への参照
        if child is not None:
            child.parent = denode.parent

        # denodeの上から下への参照
        if denode.is_root():
            self.root = denode
        elif denode.parent.left == denode:
            denode.parent.left = child
        else:
            denode.parent.right = child

        if denode is not node:
            node.key = denode.key
        del denode

def main():
    n = int(input())
    tree = Tree()
    for _ in range(n):
        operation = input()
        if operation[0] == "i":
            tree.insert(int(operation.split()[1]))
        elif operation[0] == "f":
            if tree.find(int(operation.split()[1])) is None:
                print("no")
            else:
                print("yes")
        elif operation[0] == "d":
            tree.delete(int(operation.split()[1]))
        else:
            print(" {}".format(" ".join(map(str, tree.inorder()))))
            print(" {}".format(" ".join(map(str, tree.preorder()))))


if __name__ == "__main__":
    main()

