class Tree:
    def __init__(self, node, children):
        self.node = node
       
        if children[0] == -1 and children[1] == -1:
            self.left = None
            self.right = None
            self.children = []
        elif children[0] != -1 and children[1] == -1:
            self.left = children[0]
            self.right = None
            self.children = [self.left, None]
        elif children[0] == -1 and children[1] != -1:
            self.left = None
            self.right = children[1]
            self.children =[None, children[1]]
        else:
            self.left = children[0]
            self.right = children[1]
            self.children = [self.left, self.right]

n = int(input())
NODES = {}
ROOT_SEARCH = [True]*n

for _ in range(n):
    datum = list(map(int, input().split()))
    tmp = Tree(datum[0], datum[1:])
    NODES[datum[0]] = tmp
    for element in tmp.children:
        try:
            ROOT_SEARCH[element] = False
        except:
            pass
        
for node in range(len(ROOT_SEARCH)):
    if ROOT_SEARCH[node]:
        root = node

        
In_result = []
def Inorder(NODES, root):
    global In_result
    
    if NODES[root].left != None and NODES[root].right != None:
        Inorder(NODES, NODES[root].left)
        In_result.append(root)
        Inorder(NODES, NODES[root].right)
    
    elif NODES[root].left !=None and NODES[root].right == None:
        Inorder(NODES, NODES[root].left)
        In_result.append(root)
    
    elif NODES[root].left == None and NODES[root].right != None:
        In_result.append(root)
        Inorder(NODES, NODES[root].right)
    
    else:
        In_result.append(root)

Post_result = []
def Postorder(NODES, root):
    global Post_result
    
    if NODES[root].left != None and NODES[root].right != None:
        Postorder(NODES, NODES[root].left)
        Postorder(NODES, NODES[root].right)
        Post_result.append(root)
    
    elif NODES[root].left !=None and NODES[root].right == None:
        Postorder(NODES, NODES[root].left)
        Post_result.append(root)
    
    elif NODES[root].left == None and NODES[root].right != None:
        Postorder(NODES, NODES[root].right)
        Post_result.append(root)
    
    else:
        Post_result.append(root)

Pre_result=[]
def Preorder(NODES, root):
    global Pre_result
    
    if NODES[root].left != None and NODES[root].right != None:
        Pre_result.append(root)
        Preorder(NODES, NODES[root].left)
        Preorder(NODES, NODES[root].right)
    
    elif NODES[root].left !=None and NODES[root].right == None:
        Pre_result.append(root)
        Preorder(NODES, NODES[root].left)
    
    elif NODES[root].left == None and NODES[root].right != None:
        Pre_result.append(root)
        Preorder(NODES, NODES[root].right)
    
    else:
        Pre_result.append(root)

Pre_result_str  = list(map(str, Pre_result))
Post_result_str = list(map(str, Post_result))
In_result_str   = list(map(str, In_result))

print("Preorder")
Preorder(NODES, root)
print(" "+" ".join(map(str, Pre_result)))

print("Inorder")
Inorder(NODES, root)
print(" "+" ".join(map(str, In_result)))

print("Postorder")
Postorder(NODES, root)
print(" "+" ".join(map(str, Post_result)))
