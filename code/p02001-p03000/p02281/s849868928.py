import sys

def preorder_tree_walk(nid, route):
    left = nodes[nid][1]
    right = nodes[nid][2]
    route.append(nid)
    if left != -1: preorder_tree_walk(left, route)
    if right != -1: preorder_tree_walk(right, route)
    return route

def inorder_tree_walk(nid, route):
    left = nodes[nid][1]
    right = nodes[nid][2]
    if left != -1: inorder_tree_walk(left, route)
    route.append(nid)
    if right != -1: inorder_tree_walk(right, route)
    return route

def postorder_tree_walk(nid, route):
    left = nodes[nid][1]
    right = nodes[nid][2]
    if left != -1: postorder_tree_walk(left, route)
    if right != -1: postorder_tree_walk(right, route)
    route.append(nid)
    return route

n = int(input())
nodes = [[-1, -1, -1] for _ in range(n)]

for _ in range(n):
    nid, left, right = list(map(int, sys.stdin.readline().split()))
    nodes[nid][1] = left
    nodes[nid][2] = right

    if left != -1: nodes[left][0] = nid
    if right != -1: nodes[right][0] = nid

for nid, node in enumerate(nodes):
    root_nid = nid
    if node[0] == -1: break

preorder_route = preorder_tree_walk(root_nid, [])
inorder_route = inorder_tree_walk(root_nid, [])
postorder_route = postorder_tree_walk(root_nid, [])

print('Preorder')
print('', *preorder_route)
print('Inorder')
print('', *inorder_route)
print('Postorder')
print('', *postorder_route)
