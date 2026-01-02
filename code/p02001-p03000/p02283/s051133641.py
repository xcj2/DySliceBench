class node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class Tree(object):
    def __init__(self):
        self.root = None

def insert(T,z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right
    
    z.parent = y
    if y == None:
        T.root = z
    elif z.value < y.value:
        y.left = z
    else :
        y.right = z

# 先行順巡回
def preorder(node):
    if node is None:
        return 
    print(" "+str(node.value),end="")    
    preorder(node.left)
    preorder(node.right)
    
# 中間順巡回 
def inorder(node):
    if node is None:
        return 
    inorder(node.left)
    print(" "+str(node.value),end="")
    inorder(node.right)
    
def print_all_node(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print("p: ",node.parent,"r:",node.right,"l:",node.left)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

if __name__ == "__main__":
    n = int(input())
    T = Tree()
    queries = [input().split() for _ in range(n)]
    for query in queries:
        if query[0] == "print":
            #print_all_node(T.root)
            inorder(T.root)
            print("")
            preorder(T.root)
            print("")

        else:
            command,value = query
            node_z = node()
            node_z.value = int(value)
            if command == "insert":
                insert(T,node_z)

