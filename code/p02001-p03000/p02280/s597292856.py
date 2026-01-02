class Node:
    def __init__(self):
        self.parent = -1
        self.degree = 0
        self.sibling = -1

def cal_depth(node_id, d = 0):
    Tree[node_id].depth = d
    if Tree[node_id].left !=-1:
        cal_depth(Tree[node_id].left, d+1)
    if Tree[node_id].right !=-1:
        cal_depth(Tree[node_id].right, d+1)
        
def cal_height(node_id):
    left_h = 0
    right_h = 0
    if Tree[node_id].left != -1:
        left_h = cal_height(Tree[node_id].left) + 1
    if Tree[node_id].right != -1:
        right_h = cal_height(Tree[node_id].right) + 1
    Tree[node_id].height = max(left_h, right_h)
    return max(left_h, right_h)
    
    
    
    
    
N = int(input())
Tree = [Node() for _ in range(N)]

#make_tree
for _ in range(N):
    #id, 子供の数k, c_0~c_k
    tree_info = list(map(int, input().split()))
    node_id = tree_info[0]
    left = tree_info[1]
    right = tree_info[2]
    #自身の子をセット
    Tree[node_id].left = left
    Tree[node_id].right = right
    #子からみた親をセット
    if left != -1:
        Tree[left].parent = node_id
    if right != -1:
        Tree[right].parent = node_id
    #ノードのタイプをセット
    if left == -1 and right == -1:
        Tree[node_id].type = "leaf"
    elif left == -1 or right == -1:
        Tree[node_id].degree = 1
        Tree[node_id].type = "internal node"
    else:
        #兄弟をセット
        Tree[right].sibling = left
        Tree[left].sibling = right
        Tree[node_id].degree = 2
        Tree[node_id].type = "internal node"
        

#search_root
root_id =[i for i,t in enumerate(Tree) if t.parent == -1][0]
Tree[root_id].type = "root"
cal_depth(root_id)
cal_height(root_id)


#answer_output
for i, t in enumerate(Tree):
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, t.parent, t.sibling, t.degree, t.depth, t.height, t.type))
