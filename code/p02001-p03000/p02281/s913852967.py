import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self):
        self.id = None
        self.p = None
        self.left = None
        self.right = None

def Preorder(u):
    if u == -1:
        return
    print(' {}'.format(u), end='')
    Preorder(T[u].left)
    Preorder(T[u].right)
            
def Inorder(u):
    if u == -1:
        return
    Inorder(T[u].left)
    print(' {}'.format(u), end='')
    Inorder(T[u].right)

def Postorder(u):
    if u == -1:
        return
    Postorder(T[u].left)
    Postorder(T[u].right)
    print(' {}'.format(u), end='')

n = int(input())
T = [None] * n
for i in range(n):
    temp = Node()
    T[i] = temp

for i in range(n):
    d = 0
    L = [int(x) for x in input().split()]
    v, l, r = L[0], L[1], L[2]
    T[v].id = v
    T[v].left = l
    T[v].right = r
    if l != -1:
        T[l].p = v
    if r != -1:
        T[r].p = v

for i, t in enumerate(T):
    if t.p == None:
        t.p = -1
        root = i

print('Preorder')
Preorder(T[root].id)
print('\nInorder')
Inorder(T[root].id)
print('\nPostorder')
Postorder(T[root].id)
print('')
