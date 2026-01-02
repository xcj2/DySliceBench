def print_node(i, node):
    parent = -1 if node[1] == None else node[1]
    degree = len([x for x in node[0] if x != -1])
    sibling = -1 if node[2] == None else node[2]
    depth = node[3]
    height = node[4]
    t = 'root' if parent == -1 else 'leaf' if height == 0 else 'internal node'
    ans = "node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, parent, sibling, degree, depth, height, t)
    print(ans)

n = int(input())

root = set([x for x in range(n)])
T = [None] * n
for x in range(n):
    i, l, r = list(map(int, input().split()))

    # children, parent, sibling, depth, height
    T[i] = [[l, r], None, None, None, None]
    root -= set([l, r])

def set_info(i, depth):
    node = T[i]
    node[3] = depth
    l = None
    r = None
    if node[0][0] != -1:
        l = T[node[0][0]]
        l[1] = i
        set_info(node[0][0], depth + 1)
    if node[0][1] != -1:
        r = T[node[0][1]]
        r[1] = i
        set_info(node[0][1], depth + 1)
    if l != None and r != None:
        l[2] = node[0][1]
        r[2] = node[0][0]

    node[4] = height(i)

def height(i):
    node = T[i]
    l = node[0][0]
    r = node[0][1]
    lh = None
    rh = None
    h = None
    if l != -1:
        lh = height(l)
    if r != -1:
        rh = height(r)
    if lh != None and rh != None:
        h = max(lh, rh)
    elif lh != None:
        h = lh
    elif rh != None:
        h = rh
    if h == None:
        return 0
    else:
        return 1 + h


r = root.pop()
T[r][1] = -1
set_info(r, 0)

for i, n in enumerate(T):
    print_node(i, n)