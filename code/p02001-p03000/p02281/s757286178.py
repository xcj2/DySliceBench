
class Node():
    "node of the tree structure"
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right
def preParse(u):
    if u == -1:
        return
    list_preParse.append(u)
    preParse(node_list[u].left)
    preParse(node_list[u].right)

def inParse(u):
    if u == -1:
        return
    inParse(node_list[u].left)
    list_inParse.append(u)
    inParse(node_list[u].right)

def postParse(u):
    if u == -1:
        return
    postParse(node_list[u].left)
    postParse(node_list[u].right)
    list_postParse.append(u)

def returnRoot(u):
    while node_list[u].parent != -1:
        u = node_list[u].parent
    return u

list_preParse = []
list_inParse = []
list_postParse = []
n = int(input())
node_list = []
for i in range(n):
    node = Node()
    node_list.append(node)

for i in range(n):
    a,b,c = map(int, input().split())
    node_list[a].left = b
    node_list[a].right = c
    if b != -1:
        node_list[b].parent = a
    if c != -1:
        node_list[c].parent = a

print("Preorder")
preParse(returnRoot(0))
for i in range(n):
    list_preParse[i] = str(list_preParse[i])
print(" " + " ".join(list_preParse))

print("Inorder")
inParse(returnRoot(0))
for i in range(n):
    list_inParse[i] = str(list_inParse[i])
print(" " + " ".join(list_inParse))
print("Postorder")
postParse(returnRoot(0))
for i in range(n):
    list_postParse[i] = str(list_postParse[i])
print(" " + " ".join(list_postParse))

