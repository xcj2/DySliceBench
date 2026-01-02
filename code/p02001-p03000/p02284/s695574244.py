# coding=utf-8

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        flag = False

        if self.root == None:
            self.root = node
        else:
            search_node = self.root
            while search_node:
                final_node = search_node
                if final_node.key < key:
                    search_node = final_node.right
                    flag = 'right'
                else:
                    search_node = final_node.left
                    flag = 'left'
            node.parent = final_node
            if flag == 'right':
                final_node.right = node
            elif flag == 'left':
                final_node.left = node

    def tprint(self):
        self.root.inwalk()
        print()
        self.root.prewalk()
        print()

    def find(self, key):
        if self.root.find(key):
            print('yes')
        else:
            print('no')


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def prewalk(self):
        print(" " + str(self.key), end = "")
        if self.left:
            self.left.prewalk()
        if self.right:
            self.right.prewalk()

    def inwalk(self):
        if self.left:
            self.left.inwalk()
        print(' ' + str(self.key), end = "")
        if self.right:
            self.right.inwalk()

    def find(self, key):
        find_flag = False
        node = self

        while node != None:
            if key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            elif key == node.key:
                find_flag = True
                break

        return find_flag


n = int(input())
tree = Tree()

for _ in range(n):
    order, *key = input().split()
    if order == 'insert':
        tree.insert(int(key[0]))

    elif order == 'find':
        tree.find(int(key[0]))

    elif order == 'print':
        tree.tprint()