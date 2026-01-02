class Node:
    def __init__(self):
        self.parent = -1
        self.degree = 0
        self.sibling = -1

def make_orderlist(node_id, answer_dic):
    preorder(node_id, answer_dic)
    inorder(node_id, answer_dic)
    postorder(node_id,answer_dic)

def preorder(node_id, answer_dic):
    if node_id == -1:
        return
    answer_dic["Preorder"].append(str(node_id))
    preorder(Tree[node_id].left, answer_dic)
    preorder(Tree[node_id].right, answer_dic)
    
def inorder(node_id, answer_dic):
    if node_id == -1:
        return
    inorder(Tree[node_id].left, answer_dic)
    answer_dic["Inorder"].append(str(node_id))
    inorder(Tree[node_id].right, answer_dic)

def postorder(node_id, answer_dic):
    if node_id == -1:
        return
    postorder(Tree[node_id].left, answer_dic)
    postorder(Tree[node_id].right, answer_dic)
    answer_dic["Postorder"].append(str(node_id))
    

N = int(input())
Tree = [Node() for _ in range(N)]

#make_tree
for _ in range(N):
    #id, left, right
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
    if left != -1 and right != -1:
        #兄弟をセット
        Tree[right].sibling = left
        Tree[left].sibling = right
        
#search_root
root_id =[i for i,t in enumerate(Tree) if t.parent == -1][0]
answer_dic = {"Preorder":[], "Inorder":[], "Postorder":[]}
make_orderlist(root_id, answer_dic)

#answer_output
for i in answer_dic:    
    print(i)
    print(" "+" ".join(answer_dic[i]))
