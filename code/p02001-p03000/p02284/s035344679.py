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
        if self.root == None:
            return False
        else:
            curr_node = self.root
            while curr_node:
                if key == curr_node.val:
                    return True
                elif key < curr_node.val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            return False
            
        
        
        
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
        if flag:
            print('yes')
        else:
            print('no')
    if com[0] == 'print':
        In = T.inorderTraversal(T.root)
        Pre = T.preorderTraversal(T.root)
        print(' ' + ' '.join(list(map(str, In))))
        print(' ' + ' '.join(list(map(str, Pre))))

