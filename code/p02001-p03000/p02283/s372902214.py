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

    def print_tree(self):
        prewalked = self.root.prewalk()
        inwalked = self.root.inwalk()
        print(' ', end = '')
        print(*inwalked)
        print(' ', end = '')
        print(*prewalked)


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def prewalk(self):
        result = []
        result += [self.key] # ??¢?´¢????????? #
        if self.left:
            result += self.left.prewalk()
        if self.right:
            result += self.right.prewalk()
        #print("self.key:", self.key, result) #debugger
        return result



    def inwalk(self):
        result = []
        if self.left:
            result += self.left.inwalk()
        result += [self.key] # ??¢?´¢????????? #
        if self.right:
            result += self.right.inwalk()
        #print("self.key:", self.key, result) #debugger
        return result


n = int(input())
tree = Tree()
for _ in range(n):
    order, *key = input().split()
    if order == 'insert':
        tree.insert(int(key[0]))
    else:
        tree.print_tree()