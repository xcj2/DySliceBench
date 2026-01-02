class BinaryTree:
    def __init__(self, node, children):
        self.node = node
        for i in range(2):
            try:
                children.remove(-1)
            except:
                pass
            
        self.children = children
        self.parent = -1
        try:
            self.sibling = self.parent.children.remove(self.node)[0]
        except:
            self.sibling = -1
        
        self.degree = len(children)
        self.depth = 0
        self.height = 0
        if len(children) == 0:    #子が両方とも-1の場合
            self.status = "leaf"
        else:
            self.status="root"
    
    def display(self):
        print("""node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s"""
             %(self.node, self.parent, self.sibling, self.degree, self.depth, self.height, self.status))

n = int(input())
NODE_DICT = {}
root_search = {}
for loop in range(n):
    tmp_input = list(map(int, input().split()))
    tmp = BinaryTree(tmp_input[0], tmp_input[1:])
    NODE_DICT[tmp_input[0]] = tmp
    root_search[tmp_input[0]] = True
    
for loop in range(n):
    for element in NODE_DICT[loop].children:
        root_search[element] = False

for element in range(n):
    if root_search[element]:
        root = element

def Process(NODE_DICT, node, depth):
    
    NODE_DICT[node].depth = depth
    
    if len(NODE_DICT[node].children) != 0:
        if depth != 0:
            NODE_DICT[node].status = "internal node"
        height_list = []
        if len(NODE_DICT[node].children) == 2:
            NODE_DICT[NODE_DICT[node].children[0]].sibling, NODE_DICT[NODE_DICT[node].children[1]].sibling \
            = NODE_DICT[node].children[1], NODE_DICT[node].children[0]
        
        for child in NODE_DICT[node].children:
            NODE_DICT[child].parent = NODE_DICT[node].node
            Process(NODE_DICT, child, depth+1)
            height_list.append(NODE_DICT[child].height+1)
            
        NODE_DICT[node].height = max(height_list)
        
    else:
        if depth == 0:
            NODE_DICT[node].status = "root"
        NODE_DICT[node].height = 0
    
Process(NODE_DICT, root, 0)

for loop in range(len(NODE_DICT)):
    NODE_DICT[loop].display()
