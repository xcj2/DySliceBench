class Node():
    key = 0
    l = None
    r = None
    def __init__(self, key):
        self.key = key
T = [None] * 5000005
def insert(z):
    if z == 0: return
    y = 0
    x = 0
    while x is not None:
        y = x
        x = (T[x].l if T[z].key < T[x].key else T[x].r)
    if T[z].key < T[y].key : T[y].l = z
    else : T[y].r = z
def inorder(x):
    if x == None: return;
    inorder(T[x].l);
    print("", T[x].key, end="")
    inorder(T[x].r);
def preorder(x):
    if x == None: return;
    print("", T[x].key, end="")
    preorder(T[x].l);
    preorder(T[x].r);
n = int(input())
for i in range(n):
    s = input()
    if s == "print":
        inorder(0)
        print()
        preorder(0)
        print()
    else:
        x = int(s.split()[1])
        T[i] = Node(x)
        insert(i)