import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

def preParse(T, u):
    if u == -1:
        return
    print(' {}'.format(u), end='')
    preParse(T, T[u].left)
    preParse(T, T[u].right)

def inParse(T, u):
    if u == -1:
        return
    inParse(T, T[u].left)
    print(' {}'.format(u), end='')
    inParse(T, T[u].right)

def postParse(T, u):
    if u == -1:
        return
    postParse(T, T[u].left)
    postParse(T, T[u].right)
    print(' {}'.format(u), end='')

def main():
    N = int(input())
    T = [Node() for _ in range(N)]
    for _ in range(N):
        idx, l, r = map(int, input().split())
        T[idx].left = l
        T[idx].right = r
        if l != -1:
            T[l].parent = idx
        if r != -1:
            T[r].parent = idx
    root = [i for i, x in enumerate(T) if x.parent == -1][0]
    print('Preorder')
    preParse(T, root)
    print()
    print('Inorder')
    inParse(T, root)
    print()
    print('Postorder')
    postParse(T, root)
    print()

if __name__ == '__main__': main()
