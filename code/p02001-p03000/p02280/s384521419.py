n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
B = [lst[i][0] for i in range(n)]
node = [[] for i in range(n)]

def Insertion_Sort(lst,B,n):
    for i in range(1,n):
        v = B[i]
        w = lst[i]
        j = i-1
        while j>=0 and B[j]>v:
            B[j+1]=B[j]
            lst[j+1]=lst[j]
            j-=1
        B[j+1]=v
        lst[j+1]=w
        
def find_root():
    A = []
    for i in range(n):
        A.extend(lst[i][1:])
    for i in range(n):
        if not i in A:
            return i

def make_node(arg_parent, arg_sibling, arg_num, arg_depth):
    if arg_num == root:
        type = "root"
    elif lst[arg_num][1] == lst[arg_num][2] == -1:
        type = "leaf"
    else:
        type = "internal node"
    children_lst = lst[arg_num][1:]
    degree = 0
    for i in children_lst:
        if i != -1:
            degree+=1
    height = -1
    node[arg_num] = [arg_parent, arg_sibling, degree, arg_depth, height, type]
    if children_lst[0]!=-1:
        make_node(arg_num, children_lst[1], children_lst[0], arg_depth+1)
    if children_lst[1]!=-1:
        make_node(arg_num, children_lst[0], children_lst[1], arg_depth+1)

def make_height(arg_num, arg_height):
    if arg_height > node[arg_num][4]:
        node[arg_num][4] = arg_height
        if node[arg_num][0] != -1:
            make_height(node[arg_num][0], arg_height+1)

def make_height_0_list():
    A = []
    for i in range(n):
        if node[i][2] == 0:
            A.append(i)
    return A

Insertion_Sort(lst, B, n)
root = find_root()
make_node(-1, -1, root, 0)
height_0_list = make_height_0_list()
for i in height_0_list:
    make_height(i, 0)

for i in range(n):
    parent, sibling, degree, depth, height, type = node[i]
    print(f"node {i}: parent = {parent}, sibling = {sibling}, degree = {degree}, depth = {depth}, height = {height}, {type}")
