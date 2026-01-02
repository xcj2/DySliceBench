N = int(input())
T = [list(map(int,input().split())) for _ in range(N)]

T.sort(key = lambda x:x[0])

class Node:
    def __init__(self,data,l_child,r_child):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

T = [Node(T[i][0],T[i][1],T[i][2]) for i in range(N)]

P = [-1 for _ in range(N)]
for i in range(N):
    if T[i].l_child != -1:
        P[T[i].l_child] = T[i].data
    if T[i].r_child != -1:
        P[T[i].r_child] =T[i].data
for i in range(N):
    if P[i] == -1:
        root = i

def Pre_patrol(node,List):
    if node.data != -1:
        List.append(node.data)
        if node.l_child != -1:
            Pre_patrol(T[node.l_child],List)
        if node.r_child != -1:
            Pre_patrol(T[node.r_child],List)
    return List

def In_patrol(node,List):
    if node.data != -1:
        if node.l_child != -1:
            In_patrol(T[node.l_child],List)
        List.append(node.data)
        if node.r_child != -1:
            In_patrol(T[node.r_child],List)
    return List

def Pos_patrol(node,List):
    if node.data != -1:
        if node.l_child != -1:
            Pos_patrol(T[node.l_child],List)
        if node.r_child != -1:
            Pos_patrol(T[node.r_child],List)
        List.append(node.data)
    return List

print("Preorder")
for i in range(N):
    print(" "+str(Pre_patrol(T[root],[])[i]),end="")
print()
print("Inorder")
for i in range(N):
    print(" "+str(In_patrol(T[root],[])[i]),end="")
print()
print("Postorder")
for i in range(N):
    print(" "+str(Pos_patrol(T[root],[])[i]),end="")
print()

