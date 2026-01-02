class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling=-1
        self.degree=2
        self.height=None

    def get_depth(self):
        if self.parent == -1:
            return 0
        else:
            depth = 1
            t = Nodes[self.parent]
            while t.parent != -1:
                t=Nodes[t.parent]
                depth += 1
            return depth
    
    def get_height(self):
        height = 0
        height2 = 0

        if self.right != -1:
            t = Nodes[self.right]
            height =t.get_height()+1

        if self.left != -1:
            t2 = Nodes[self.left]
            height2=t2.get_height()+1
            # height2 += 1

        self.height=max(height,height2)
        return self.height

    def get_type(self):
        if self.parent == -1:
            return 'root'
        elif self.left == -1 and self.right == -1:
            self.degree=0
            return 'leaf'
        else:
            return 'internal node'

    def get_degree(self):
        degree = 0
        if self.left != -1:
            degree += 1
        if self.right != -1:
            degree += 1
        return degree

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
            Nodes[left].sibling=right
            Nodes[left].parent=id
        
        Nodes[id].right = right
        if right !=-1 :
            Nodes[right].sibling=left
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

    for node_id in range(num_of_nodes):
        type = Nodes[node_id].get_type()
        p=Nodes[node_id]

        print('''node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'''.format(
            node_id, p.parent,p.sibling,p.get_degree(), p.get_depth(), p.get_height(), type))
