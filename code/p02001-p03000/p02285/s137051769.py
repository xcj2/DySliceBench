class Node:
    def __init__(self, value, parent):
        self.val = value
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        node = Node(key, None)
        if self.root == None:
            self.root = node
        else:
            curr_node = self.root
            while curr_node:
                parent_node = curr_node
                if key < curr_node.val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            node.parent = parent_node
            if key < parent_node.val:
                parent_node.left = node
            else:
                parent_node.right = node
     
    def find(self, key):
        curr_node = self.root
        while curr_node and curr_node.val != key:
            if curr_node.val < key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return curr_node
    
    # def getMax(self, node):
    #     while node.right:
    #         node = node.right
    #     return node
    
    # def getNode(self, key):
    #     curr_node = self.root
    #     while curr_node and curr_node.val != key:
    #         if key < curr_node.val:
    #             curr_node = curr_node.left
    #         else:
    #             curr_node = curr_node.right
    #     return curr_node   

    def getMinimum(self, node):
        while node.left:
            node = node.left
        return node

    def getSuccessor(self,node):
        if node.right:
            return self.getMinimum(node.right)

        parent_node = node.parent
        while parent_node and node != parent_node.left:
            node = parent_node
            parent_node = node.parent
        return parent_node
    
    def delete(self, key):
        node = self.find(key)
        if node:
            if node.left == None or node.right == None:
                y = node
            else:
                y = self.getSuccessor(node)

            if y.left != None:
                x = y.left
            else:
                x = y.right

            if x != None:
                x.parent = y.parent

            if y.parent == None:
                self.root = x
            elif y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x

            if y != node:
                node.val = y.val


    def preorderTraversal(self, node):
        result = []
        if node == None:
            return result
        result += [node.val]
        result += self.preorderTraversal(node.left)
        result += self.preorderTraversal(node.right)
        return result 


        
    def inorderTraversal(self, node):
        result = []
        if node == None:
            return result
        result += self.inorderTraversal(node.left)
        result += [node.val]
        result += self.inorderTraversal(node.right)
        return result

N = int(input())
command = []
for i in range(N):
    command.append(tuple(input().split()))

T = BinarySearchTree()
for com in command:
    if com[0] == 'insert':
        T.insert(int(com[1]))
    if com[0] == 'find':
        flag = T.find(int(com[1]))
        if flag != None:
            print('yes')
        else:
            print('no')
    if com[0] == 'delete':
        T.delete(int(com[1]))
    if com[0] == 'print':
        In = T.inorderTraversal(T.root)
        Pre = T.preorderTraversal(T.root)
        print(' ' + ' '.join(list(map(str, In))))
        print(' ' + ' '.join(list(map(str, Pre))))

