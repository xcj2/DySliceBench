class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.value_dic = {}
    
    def is_find(self,value):
        if value in self.value_dic:
            return True
        else:
            return False
    
    def find(self,value):
        node = T.root

        while node :
            if value == node.value:
                break
            elif value > node.value:
                node = node.right
            else :
                node = node.left
        return node

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

    T.value_dic[z.value] = 1

def getMinimum(z):
    while z.left != None:
        z = z.left
    return z

def getSuccessor(z):
    if z.right != None:
        return getMinimum(z.right)

    y = z.parent
    while y != None and z == y.right:
        z = y
        y = y.parent
    return y

def delete(T,z):
    # 削除する対象をyとする
    if z.left is None or z.right is None:
        y = z
    else:
        y = getSuccessor(z)

    # 子をxとする
    if y.left != None:
        x = y.left
    else:
        x = y.right
    

    # 子がいる場合
    if x != None:
        x.parent = y.parent
    
    if y.parent is None:
        T.root = x
    elif y.parent.left == y:
        y.parent.left = x
    else:
        y.parent.right = x
    
    if y != z:
        z.value = y.value



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
            if command == "insert":
                node_z = Node()
                node_z.value = int(value)
                insert(T,node_z)
            elif command == "find":
                if T.is_find(int(value)):
                    print("yes")
                else:
                    print("no")
            elif command == "delete":
                node = T.find(int(value))
                if node:
                    T.value_dic.pop(int(value))
                delete(T,node)
