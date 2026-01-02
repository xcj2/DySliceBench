class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

def bst_insert(node, label):
    if node is None:
        return Node(label)

    elif label< node.label:
        node.left = bst_insert(node.left, label)
    else:
        node.right = bst_insert(node.right, label)
    return node

def bst_find(node, label):
    if node is None:
        return False
    elif label == node.label:
        return True
    elif label< node.label:
        return bst_find(node.left, label)
    elif label > node.label:
        return bst_find(node.right, label)




def bst_inorder(node):
    global In
    if (node.left is not None):
        bst_inorder(node.left)
    In.append(node.label)
    if (node.right is not None):
        bst_inorder(node.right)
    return

def bst_preorder(node):
    global Pre
    Pre.append(node.label)
    if (node.left is not None):
        bst_preorder(node.left)
    if (node.right is not None):
        bst_preorder(node.right)
    return

n= int(input())
tree = None
for i in range(n):
    cmmd = list(input().split( ))
    if cmmd[0] == "insert":
        k =int(cmmd[1])
        tree = bst_insert(tree, k)
    elif cmmd[0] == "find":
        k = int(cmmd[1])
        flag = bst_find(tree,k)
        if flag:
            print("yes")
        else:
            print("no")
        
    else:
        In =[]
        bst_inorder(tree)
        print("",*In)
        Pre =[]
        bst_preorder(tree)
        print("",*Pre)
