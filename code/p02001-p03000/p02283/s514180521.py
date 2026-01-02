class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        root_node = self.root
        insert_node = Node(key)
        parent_node = None

        while root_node:
            parent_node = root_node
            if insert_node.key < root_node.key:
                root_node = root_node.left
            else:
                root_node = root_node.right

        insert_node.parent = parent_node

        if parent_node is None:
            self.root = insert_node
        elif insert_node.key < parent_node.key:
            parent_node.left = insert_node
        else:
            parent_node.right = insert_node

    def show_preorder(self, node):
        node_list = []

        node_list.append(node.key)
        if node.left is not None:
            node_list.extend(self.show_preorder(node.left))
        if node.right is not None:
            node_list.extend(self.show_preorder(node.right))

        return node_list

    def show_inorder(self, node):
        node_list = []

        if node.left is not None:
            node_list.extend(self.show_inorder(node.left))
        node_list.append(node.key)
        if node.right is not None:
            node_list.extend(self.show_inorder(node.right))

        return node_list

    def print(self):
        print(' ' + ' '.join(map(str, self.show_inorder(self.root))))
        print(' ' + ' '.join(map(str, self.show_preorder(self.root))))


if __name__ == '__main__':
    tree = BinarySearchTree()

    n = int(input())

    for i in range(n):
        command = input().split()

        if command[0] == 'insert':
            tree.insert(int(command[1]))
        elif command[0] == 'print':
            tree.print()