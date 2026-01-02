import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    children = [[] for _ in range(n)]
    parent = [-1]*n
    for _ in range(n):
        ilr = LI()
        id = ilr[0]
        left = ilr[1]
        right = ilr[2]
        children[id] = (left, right)
        if left>=0: parent[left] = id
        if right>=0: parent[right] = id

    preorder = []
    inorder = []
    postorder = []

    def dfs(v):
        preorder.append(v)
        c0, c1 = children[v]
        if c0!=-1:
            dfs(c0)
        inorder.append(v)
        if c1!=-1:
            dfs(c1)
        postorder.append(v)
    
    root = parent.index(-1)
    dfs(root)

    print('Preorder')
    print('', *preorder)
    print('Inorder')
    print('', *inorder)
    print('Postorder')
    print('', *postorder)

if __name__ == '__main__':
    resolve()

