class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

def preParse(u):
    if u ==-1:
        return
    print(" %d"%(u),end = "")
    # print(u,end=' ')
    preParse(Nodes[u].left)
    preParse(Nodes[u].right)

def inParse(u):
    if u ==-1:
        return
    inParse(Nodes[u].left)
    print(" %d"%(u),end = "")

    # print(u,end=' ')
    inParse(Nodes[u].right)

def postParse(u):
    if u ==-1:
        return
    postParse(Nodes[u].left)
    postParse(Nodes[u].right)
    # print(u,end=' ')
    print(" %d"%(u),end = "")



def decode_node_data(n):
    '''
    n...受け取る文字列、一行ずつ
    一行ずつ、文字列からノードに変化する
    '''
    global Nodes
    num_of_elem = len(n)
    if num_of_elem < 2:
        raise ValueError
    elif num_of_elem == 2:  # leaf
        pass

    else:
        id, left,right = list(map(int,n))
        # まず、一人目の子供をとりあえず左に格納する
        Nodes[id].left = left
        if left!=-1:
            Nodes[left].parent=id
        
        Nodes[id].right = right
        if right !=-1 :
            Nodes[right].parent=id


MAX_NODES = 100001
Nodes = [Node(-1, None, None) for _ in range(MAX_NODES)]
if __name__ == "__main__":

    num_of_nodes = int(input())
    node_data = []
    for _ in range(num_of_nodes):
        node_data.append(input().split(' '))

    for n in node_data:
        decode_node_data(n)
    
    for i in range(num_of_nodes):
        if Nodes[i].parent==-1:
            root=i
    
    print('Preorder')
    preParse(root)
    print()
    
    print('Inorder')
    inParse(root)
    print()
    
    print('Postorder')
    postParse(root)
    print()



