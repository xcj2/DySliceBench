class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right
def postorder(ns,i, post):
    if ns[i].left != -1:
        postorder(ns,ns[i].left ,post)
    if ns[i].right != -1:
        postorder(ns,ns[i].right ,post)
    post.append(str(i+1))
def poio_node(ns,po,io):
    root = po[0]
    i = io.index(root)
    if i!=0: # root의 왼쪽노드가 존재한다면 왼쪽으로 재귀
        ns[po[0]].left = po[1]
        ns[po[1]].parent = po[0]
        poio_node(ns,po[1:i+1],io[:i]) # po, io 안의 왼쪽 노드들로만 재귀
    if i!=len(io)-1: # root의 오른쪽 노드가 존재한다면 오른쪽으로 재귀
        ns[po[0]].right = po[i+1]
        ns[po[i+1]].parent = po[0]
        poio_node(ns, po[i+1:], io[i+1:]) # po, io 안의 오른쪽 노드들로만 재귀
def min1(n):
    return (n-1)
n = int(input())
po = list(map(int,input().split()))
io = list(map(int,input().split()))
po = list(map(min1,po))   ##0~(n-1)로 변환
io = list(map(min1,io))
ns =  [Node()for i in range(n)]

poio_node(ns, po, io)

post = []
postorder(ns, po[0], post)
print(" ".join(post))
