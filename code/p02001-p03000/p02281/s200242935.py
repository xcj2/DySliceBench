class BinaryTree:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

n = int(input().rstrip())

T = []
for _ in range(n):
    T.append(BinaryTree(-1, -1, -1))

for _ in range(n):
    input_line = list(map(int, input().rstrip().split(" ")))
    assert len(input_line) == 3, "input line should be composed of 3 items"
    u, left, right = input_line
    T[u].left = left
    T[u].right = right
    if left != -1:
        T[left].parent = u
    if right != -1:
        T[right].parent = u

def preParse(u):
    if u == -1:
        return 0
    print(" " + str(u), end="")
    preParse(T[u].left)
    preParse(T[u].right)

def inParse(u):
    if u == -1:
        return 0
    inParse(T[u].left)
    print(" " + str(u), end="")
    inParse(T[u].right)

def postParse(u):
    if u == -1:
        return 0
    postParse(T[u].left)
    postParse(T[u].right)
    print(" " + str(u), end="")

# find parent
for u, t in enumerate(T):
    if t.parent == -1:
        parent = u
        break
        

print("Preorder")
preParse(parent)
print()
print("Inorder")
inParse(parent)
print()
print("Postorder")
postParse(parent)
print()
