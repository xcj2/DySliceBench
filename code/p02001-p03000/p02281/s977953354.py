def getroot():
    return [key for key,node in nodes.items() if node[0] == -1][0]

def Preorder(id):
    yield id
    for child_id in (child_id for child_id in nodes[id][1:] if child_id != -1):
        yield from Preorder(child_id)

def Inorder(id):
    if nodes[id][1] != -1:
        yield from Inorder(nodes[id][1])
    yield id
    if nodes[id][2] != -1:
        yield from Inorder(nodes[id][2])

def Postorder(id):
    for child_id in (child_id for child_id in nodes[id][1:] if child_id != -1):
        yield from Postorder(child_id)
    yield id

nodes = dict()
n = int(input())
for _ in range(n):
    id,l,r = list(map(int, input().split()))
    if id not in nodes:
        nodes[id] = (-1, -1, -1)
    node = nodes[id]
    node = (node[0], l, r)
    nodes[id] = node
    for child_id in [child_id for child_id in node[1:] if child_id != -1]:
        if child_id not in nodes:
            nodes[child_id] = (-1, -1, -1)
        child_node = nodes[child_id]
        child_node = (id, child_node[1], child_node[2])
        nodes[child_id] = child_node

rootid = getroot()
print("Preorder")
print(" ", end="")
print(*Preorder(rootid))
print("Inorder")
print(" ", end="")
print(*Inorder(rootid))
print("Postorder")
print(" ", end="")
print(*Postorder(rootid))
