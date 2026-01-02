import sys
sys.setrecursionlimit(10**7)

noded = {}
edad = {}

class Node:
    def __init__(self, index):
        self.index = index
        self.color = -1
        self.eda_list = []

class Eda:
    def __init__(self, index, w, left, right):
        self.index = index
        self.w = w
        self.left = left
        self.right = right

def color_oppo_of(node):
    c = node.color
    for eda in [edad[edai] for edai in node.eda_list]:
        if eda.right == node.index:
            oppo = eda.left
        else:
            oppo = eda.right

        if noded[oppo].color == -1:
            if eda.w % 2 == 0:
                noded[oppo].color = node.color
            else:
                noded[oppo].color = (node.color + 1) % 2
            color_oppo_of(noded[oppo])

def solve():
    n = int(input())
    if n == 1:
        print("0")
    else:
        do(n)


def do(n):
    for i in range(n-1):
        U, V, W = map(int, input().split())
        u = U
        v = V
        w = W

        eda = Eda(i, w, u, v)
        edad[i] = eda

        if u not in noded.keys():
            noded[u] = Node(u)
        noded[u].eda_list.append(i)

        if v not in noded.keys():
            noded[v] = Node(v)
        noded[v].eda_list.append(i)

    noded[1].color = 0
    color_oppo_of(noded[1])

    for i in range(1, n+1):
        print(noded[i].color)
        #print(vars(noded[i]))



solve()