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
        A.extend(lst[i][2:])
    for i in range(n):
        if not i in A:
            return i

def make_node(arg_parent,arg_num, arg_depth):
    if arg_num == root:
        type = "root"
    elif lst[arg_num][1] == 0:
        type = "leaf"
    else:
        type = "internal node"
    children_lst = lst[arg_num][2:]
    node[arg_num] = [arg_parent, arg_depth, type, children_lst]
    for i in children_lst:
        make_node(arg_num, i, arg_depth+1)

Insertion_Sort(lst, B, n)
root = find_root()
make_node(-1, root, 0)

for i in range(n):
    parent, depth, type, children_lst = node[i]
    print(f"node {i}: parent = {parent}, depth = {depth}, {type}, {children_lst}")
