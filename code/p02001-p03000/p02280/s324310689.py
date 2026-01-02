n = int(input())
parent = [-1] * n
left   = [-1] * n
right  = [-1] * n
sibling = [-1] * n
degree  =  [0] * n
depth   =  [0] * n
for i in range(n):
    x = list(map(int, input().split()))
    left[x[0]]  = x[1]
    right[x[0]] = x[2]
    children = 0
    if x[1] != -1:
        parent[x[1]] = x[0]
        sibling[x[1]] = x[2]
        children += 1
    if x[2] != -1:
        parent[x[2]] = x[0]
        sibling[x[2]] = x[1]
        children += 1
    degree[x[0]] = children
def setDepth(u, p, d):
    d[u] = p
    if right[u] != -1:
        setDepth(right[u], p + 1, d)
    if left[u] != -1:
        setDepth(left[u], p + 1, d)
    return d
def getHeight(u, p, height):
    height += [p]
    if right[u] != -1:
        getHeight(right[u], p + 1, height)
    if left[u] != -1:
        getHeight(left[u], p + 1, height)
    return max(height)
def howNode(u):
    if parent[u] == -1:
        return 'root'
    elif left[u] == right[u] == -1:
        return 'leaf'
    else:
        return 'internal node'
root = parent.index(-1)
setDepth(root, 0, depth)
for i in range(n):
    print('node '+str(i)+': parent = '+str(parent[i])
    +', sibling = '+str(sibling[i])+', degree = '+
    str(degree[i])+', depth = '+str(depth[i])+', height = '
    +str(getHeight(i, 0, []))+', '+howNode(i))
