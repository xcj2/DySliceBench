n = int(input())
nodes = []
ref = [0] * n
for i in range(n):
    l = [int(i) for i in input().split()]
    if l[1] != -1:
        ref[l[1]] += 1
    if l[2] != -1:
        ref[l[2]] += 1
    nodes.append(l)

nodes = sorted(nodes, key=lambda x: x[0])

preorder_ans = []
inorder_ans = []
postorder_ans = []


# u: node(list)
def preorder(u):
    preorder_ans.append(u[0])
    if u[1] != -1:
        preorder(nodes[u[1]])

    if u[2] != -1:
        preorder(nodes[u[2]])


def inorder(u):
    if u[1] != -1:
        inorder(nodes[u[1]])

    inorder_ans.append(u[0])

    if u[2] != -1:
        inorder(nodes[u[2]])


def postorder(u):
    if u[1] != -1:
        postorder(nodes[u[1]])

    if u[2] != -1:
        postorder(nodes[u[2]])

    postorder_ans.append(u[0])


def format_print(l):
    print("", " ".join([str(i) for i in l]))


# print(nodes)

preorder(nodes[ref.index(0)])
inorder(nodes[ref.index(0)])
postorder(nodes[ref.index(0)])

print("Preorder")
format_print(preorder_ans)
print("Inorder")
format_print(inorder_ans)
print("Postorder")
format_print(postorder_ans)

