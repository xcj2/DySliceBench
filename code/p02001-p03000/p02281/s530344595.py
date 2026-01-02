import sys


def preorder(u):
    PRE.append(u)
    if TREE[u][1] != NIL:
        preorder(TREE[u][1])
    if TREE[u][2] != NIL:
        preorder(TREE[u][2])
        
        
def inorder(u):
    if TREE[u][1] != NIL:
        inorder(TREE[u][1])
    IN.append(u)
    if TREE[u][2] != NIL:
        inorder(TREE[u][2])


def postorder(u):
    if TREE[u][1] != NIL:
        postorder(TREE[u][1])
    if TREE[u][2] != NIL:
        postorder(TREE[u][2])
    POST.append(u)
        
        
if __name__=="__main__":
    NIL = -1
    n = int(sys.stdin.readline())
    TREE = [[NIL, NIL, NIL] for i in range(n)]
    root = set(range(n))
    PRE = []
    IN = []
    POST = []
    for inp in sys.stdin.readlines():
        inp = list(map(int, inp.split()))
        if inp[1] != NIL:
            TREE[inp[0]][1] = inp[1]
            TREE[inp[1]][0] = inp[1]
        if inp[2] != NIL:
            TREE[inp[0]][2] = inp[2]
            TREE[inp[2]][0] = inp[2]
        root -= set([inp[1], inp[2]])
    a = root.pop()
    preorder(a)
    inorder(a)
    postorder(a)
    print("Preorder")
    print(" " + " ".join(map(str, PRE)))
    print("Inorder")
    print(" " + " ".join(map(str, IN)))
    print("Postorder")
    print(" " + " ".join(map(str, POST)))