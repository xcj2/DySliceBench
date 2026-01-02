import sys

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
    
    def insert(node, x):
        if node == None:
            return Node(x)
#==============================================================================
#         elif x == node.data:
#             return node
#==============================================================================
        elif x < node.data:
            node.left = Node.insert(node.left, x)
        else:
            node.right = Node.insert(node.right, x)
        return node
    
    def find(node, x):
        if node.data == x:
            return True
        elif node.left != None and node.data > x:
            return Node.find(node.left, x)
        elif node.right != None and node.data < x:
            return Node.find(node.right, x)
        else:
            return False
        
    def delete(node, x):
        if node.data == x:
            if (node.left == None) and (node.right == None):
                return None
            elif node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                #????????????
                node.data = Node.serch_min(node.right)
                node.right = Node.delete_min(node.right)
                return node
        elif node.data > x:
            node.left =  Node.delete(node.left, x)
        else:
            node.right = Node.delete(node.right, x)
        return node
        
    def serch_min(node):
        if node.left != None:
            return Node.serch_min(node.left)
        else:
            return node.data
    
    def delete_min(node):
        if node.left == None:
            return node.right
        else:
            node.left = Node.delete_min(node.left)
            return node    
        
    def inorder_print(node):
#==============================================================================
#         if node.left != None:
#             Node.inorder_print(node.left)
#         print("",node.data,  end="")
#         if node.right != None:
#             Node.inorder_print(node.right)
#==============================================================================
        s = ""
        if node.left != None:
            s += Node.inorder_print(node.left)
        s += " " + str(node.data)
        if node.right != None:
            s += Node.inorder_print(node.right)
        return s
    def preorder_print(node):
#==============================================================================
#         print("",node.data,  end="")
#         if node.left != None:
#             Node.preorder_print(node.left)
#         if node.right != None:
#             Node.preorder_print(node.right)
#==============================================================================
        s = ""
        s += " " + str(node.data)
        if node.left != None:
            s += Node.preorder_print(node.left)    
        if node.right != None:
            s += Node.preorder_print(node.right)
        return s
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        self.root = Node.insert(self.root, x)

    def find(self, x):
        if Node.find(self.root, x):
            print("yes")
        else:
            print("no")
            
    def delete(self, x):
        self.root = Node.delete(self.root, x)
        
    def print_tree(self):
#==============================================================================
#         Node.inorder_print(self.root)
#         print()
#         Node.preorder_print(self.root)
#         print()
#==============================================================================
        s = Node.inorder_print(self.root)
        print(s)
        s = Node.preorder_print(self.root)
        print(s)
def main():
    T = BinaryTree()
    m = int(sys.stdin.readline())
    for i in range(m):
        s = sys.stdin.readline().strip()
        if(s == "print"):
            T.print_tree()
        elif s.split()[0] == "find":
            T.find(int(s.split()[1]))
        elif s.split()[0] == "delete":
            T.delete(int(s.split()[1]))
        else:
            z = int(s.split()[1])
            T.insert(z)
        #print(s)
        #T.print_tree()

if __name__ == "__main__":
    main()
    
    