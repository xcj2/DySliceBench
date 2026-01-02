n = int(input())
lson, rson = [-1]*n, [-1]*n
parent = [-1]*n
for i in range(n):
    id, ls, rs = map(int, input().split())
    lson[id], rson[id] = ls, rs
    if ls != -1:
        parent[ls] = id
    if rs != -1:
        parent[rs] = id
def pre_order(r):
    if r == -1: return
    print("", r, end = '')
    pre_order(lson[r])
    pre_order(rson[r])

def in_order(r):
    if r == -1: return
    in_order(lson[r])
    print("", r, end = '')
    in_order(rson[r])

def post_order(r):
    if r == -1: return
    post_order(lson[r])
    post_order(rson[r])
    print("", r, end = '')

for i in range(n):
    if parent[i] == -1:
        print("Preorder")
        pre_order(i)
        print("")
        print("Inorder")
        in_order(i)
        print("")
        print("Postorder")
        post_order(i)
        print("")
