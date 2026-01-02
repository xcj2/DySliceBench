# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, node, parent=None):
        if self.root is None:
            self.root = node
            return
        
        if parent is None:
            parent = self.root
            
        if node.id < parent.id:
            if parent.left:
                self.insert(node, parent.left)
            else:
                parent.left = node
                node.parent = parent
        else:
            if parent.right:
                self.insert(node, parent.right)
            else:
                parent.right = node
                node.parent = parent
    
    def walk_inorder(self, result, current_node=None):
        if current_node is None:
            current_node = self.root
        
        if current_node.left:
            self.walk_inorder(result, current_node.left)
            
        result.append(current_node.id)
        
        if current_node.right:
            self.walk_inorder(result, current_node.right)
    
    def walk_preorder(self, result, current_node=None):
        if current_node is None:
            current_node = self.root
        
        result.append(current_node.id)
        
        if current_node.left:
            self.walk_preorder(result, current_node.left)
            
        if current_node.right:
            self.walk_preorder(result, current_node.right)

    def find_node(self, id, current_node=None):
        if current_node is None:
            current_node = self.root
            
        if current_node.id == id:
            return True
        if id < current_node.id:
            if current_node.left and self.find_node(id, current_node.left):
                return True
        else:
            if current_node.right and self.find_node(id, current_node.right):
                return True
        return False

def main():
    n = int(input())
    tree = BinaryTree()
    
    for _ in range(n):
        cmd = input()
        if cmd[0] == 'p':
            result = []
            tree.walk_inorder(result)
            print('', *result)
            
            result = []
            tree.walk_preorder(result)
            print('', *result)
        elif cmd[0] == 'i':
            id = int(cmd.split()[1])
            node = Node(id)
            tree.insert(node)
        elif cmd[0] == 'f':
            id = int(cmd.split()[1])
            if tree.find_node(id):
                print('yes')
            else:
                print('no')

if __name__=='__main__':
    main()
