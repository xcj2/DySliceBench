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

        if parent_node == None:
            self.root = insert_node
        elif insert_node.key < parent_node.key:
            parent_node.left = insert_node
        else:
            parent_node.right = insert_node

    def find(self, key):
        node = self.root

        while node:
            if node.key == key:
                return node
            elif node.key < key:
                node = node.right
            else:
                node = node.left

        return None

    def delete(self, key):
        node = self.find(key)

        if node == None:
            return

        if node.left and node.right:
            next_node = node.right

            while next_node.left:
                next_node = next_node.left

            node.key = next_node.key
            node = next_node

        if node.left:
            node.left.parent =  node.parent
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.right:
            node.right.parent =  node.parent
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

    def show_preorder(self, node):
        node_list = []

        node_list.append(node.key)
        if node.left:
            node_list.extend(self.show_preorder(node.left))
        if node.right:
            node_list.extend(self.show_preorder(node.right))

        return node_list

    def show_inorder(self, node):
        node_list = []

        if node.left:
            node_list.extend(self.show_inorder(node.left))
        node_list.append(node.key)
        if node.right:
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
        elif command[0] == 'find':
            print('yes' if tree.find(int(command[1])) else 'no')
        elif command[0] == 'delete':
            tree.delete(int(command[1]))
        elif command[0] == 'print':
            tree.print()