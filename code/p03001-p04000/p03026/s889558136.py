*D, = open(0)
n = int(D[0])
 
edge = [[] for _ in range(n+1)]
v_val = [0 for _ in range(n+1)]
 
dist = {}
 
for i in range(1, n):
    a, b = map(int, D[i].split())
    edge[a].append(b)
    edge[b].append(a)
c = list(map(int, D[n].split()))
 
c = sorted(c, reverse=True)
 
# 木の端を求める
def findLeaf(edge, start=1):
    visited = [False for _ in range(len(edge))]
    next_v = edge[start]
    visited[start] = True
    count = 0
    
    while len(next_v) > 0:
        new_v = []
        for it in next_v:
    #         print(it)
            leaf = it
            for v in edge[it]:
                if not visited[v]:
                    new_v.append(v)
            visited[it] = True
        next_v = new_v
        count += 1
 
    return leaf, count
 
 
# 木の直径を求める
def findD(edge):
    leaf, _ = findLeaf(edge, 1)
    leaf, count = findLeaf(edge, leaf)
    return count
 
# 木の中心を求める
def findCenter(edge):
    leaf, _ = findLeaf(edge, 1)
    leaf, d = findLeaf(edge, leaf)
    r = d//2
 
    visited = [False for _ in range(len(edge))]
    start = leaf
    next_v = edge[start]
    # print(next_v, leaf)
    visited[start] = True
    count = 0
 
    while not r == count+1:
        new_v = []
        for it in next_v:
    #         print(it)
            leaf = it
            for v in edge[it]:
                if not visited[v]:
                    new_v.append(v)
            visited[it] = True
        next_v = new_v
        count += 1
        
    center = []
    for it in next_v:
        if len(edge[it]) > 1:
            center.append(it)
    return center
 
 
def calcCost(D, v_val):
    total = 0
    
    n = int(D[0])
    for i in range(1, n):
        a, b = map(int, D[i].split())
        total += min(v_val[a], v_val[b])
        
    return total
 
 
max_val = 0
max_v = 0
l, _ = findLeaf(edge)
for center in [l]:
    order = []
    start = center
    visited = [False for _ in range(len(edge))]
    next_v = edge[start]
    visited[start] = True
    order.append(center)
 
    # Get order from center
    while len(next_v) > 0:
        new_v = []
        for it in next_v:
    #         print(it)
            leaf = it
            for v in edge[it]:
                if not visited[v]:
                    new_v.append(v)
            visited[it] = True
            order.append(it)
        next_v = new_v
        
    # calculate cost
    v_val = [0 for _ in range(len(c)+1)]
    for i, it in enumerate(order):
        v_val[it] = c[i]
 
    val = calcCost(D, v_val)
    if val > max_val:
        max_val = val
        max_v = v_val
 
        
print(max_val)
print(' '.join(map(str, max_v[1:])))