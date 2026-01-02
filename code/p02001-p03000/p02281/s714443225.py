class node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None

def preorder(nodes,root):
    stacked = [nodes[root]]
    visited = []
    while(len(stacked)>0):
        node = stacked.pop()
        value = node.value
        left = node.left
        right = node.right
        visited.append(value)
        
        if (right not in visited) and (right != None):
            stacked.append(nodes[right])
        if (left not in visited) and (left != None):
            stacked.append(nodes[left])
    out = ""
    for i in visited:
        out += " "+str(i)
    return out

def inorder_search(cur,nodes,out_list):
    value,left,right = nodes[cur].value,nodes[cur].left,nodes[cur].right
    if left != None:
        inorder_search(left,nodes,out_list)
    out_list.append(value)
    if right != None:
        inorder_search(right,nodes,out_list)

def inorder(nodes,root):
    out_list = []
    cur = root
    inorder_search(cur,nodes,out_list)
    out = ""
    for i in out_list:
        out += " "+str(i)
    return out

def postorder_search(cur,nodes,out_list):
    value,left,right = nodes[cur].value,nodes[cur].left,nodes[cur].right

    if left != None:
        postorder_search(left,nodes,out_list)
    if right != None:
        postorder_search(right,nodes,out_list)
    out_list.append(value)

def postorder(nodes,root):
    out_list = []
    cur = root

    postorder_search(cur,nodes,out_list)
    out = ""
    for i in out_list:
        out += " "+str(i)
    return out

if __name__ == "__main__":
    n = int(input())
    nodes = [node() for _ in range(n)]
    for i in range(n):
        value,left,right = map(int,input().split())
        nodes[value].value = value
        if right != -1:
            nodes[value].right = right
            nodes[right].parent = value
        if left != -1:
            nodes[value].left = left
            nodes[left].parent = value
    root = 0
    for i in range(n):
        if nodes[i].parent is None:
            root = i

    print("Preorder")
    print(preorder(nodes,root))
    print("Inorder")
    print(inorder(nodes,root))
    print("Postorder")
    print(postorder(nodes,root))
