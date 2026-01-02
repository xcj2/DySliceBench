class Node():
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

def Preorder_Tree_Walk(T, u):    
    if u == -1:
        return
    
    print(" " + str(u), end="")
    Preorder_Tree_Walk(T, T[u].left)
    Preorder_Tree_Walk(T, T[u].right)

def Inorder_Tree_Walk(T, u):   
    if u == -1:
        return

    Inorder_Tree_Walk(T, T[u].left)
    print(" " + str(u), end="")
    Inorder_Tree_Walk(T, T[u].right)

def Postorder_Tree_Walk(T, u):    
    if u == -1:
        return

    Postorder_Tree_Walk(T, T[u].left)
    Postorder_Tree_Walk(T, T[u].right)
    print(" " + str(u), end="")

def Main():

    n = int(input())
    T = [Node(-1, -1, -1) for i in range(n)]

    for i in range(n):
        node_id, left, right = map(int, input().split())

        T[node_id].left = left
        T[node_id].right = right

        if left != -1:
            T[left].parent = node_id
        if right != -1:
            T[right].parent = node_id

    r = 0
    for i in range(len(T)):
        if T[i].parent == -1:
            r = i
            
    print("Preorder")
    Preorder_Tree_Walk(T, r)
    print()
    print("Inorder")
    Inorder_Tree_Walk(T, r)
    print()
    print("Postorder")
    Postorder_Tree_Walk(T, r)
    print()

Main()
