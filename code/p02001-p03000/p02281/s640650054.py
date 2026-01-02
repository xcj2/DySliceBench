global nodes

class Node:
    def _init__(self):
        self.left = -1
        self.right = -1
    def set(self,arg_node_left,arg_node_right):
        self.left =arg_node_left
        self.right =arg_node_right
    
def Preorder(node_id):
    print(" %d"%(node_id),end="")
    if nodes[node_id].left != -1:
        Preorder(nodes[node_id].left)
    if nodes[node_id].right != -1:
        Preorder(nodes[node_id].right)

def Inorder(node_id):
    if nodes[node_id].left != -1:
        Inorder(nodes[node_id].left)
    print(" %d"%(node_id),end="")
    if nodes[node_id].right != -1:
        Inorder(nodes[node_id].right)

def Postorder(node_id):
    if nodes[node_id].left != -1:
        Postorder(nodes[node_id].left)
    if nodes[node_id].right != -1:
        Postorder(nodes[node_id].right)
    print(" %d"%(node_id),end="")

V = int(input())
nodes = [Node() for _ in range(V)]
in_num = [0]*V
for loop in range(V):
    node_id,left,right = map(int,input().split())
    nodes[node_id].set(left,right)
    if left != -1:
        in_num[left] += 1
    if right != -1:
        in_num[right] += 1

root = -1 #rootを探す
for i in range(V): 
    if in_num[i] == 0:
        root = i
        break

print("Preorder")
Preorder(root)
print()

print('Inorder')
Inorder(root)
print()

print('Postorder')
Postorder(root)
print()
