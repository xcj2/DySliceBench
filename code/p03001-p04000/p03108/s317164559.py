N,M = map(int,input().split())
edges = []
for _ in range(M):
    a,b = map(int,input().split())
    edges.append((a-1,b-1))
edges.reverse()
parents = list(range(N))
size = [1 for _ in range(N)]
rank = [0 for _ in range(N)]

def root(x):
    px = parents[x]
    if px == x:
        return(x)
    else:
        r = root(px)
        parents[x] = r
        return(r)

def same(x,y):
    return(root(x) == root(y))

def union(x,y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return(0)
    if rank[ry] > rank[rx]:
        parents[rx] = ry
        size[ry] += size[rx]
    else:
        parents[ry] = rx
        size[rx] += size[ry]
        if rank[rx] == rank[ry]:
            rank[rx] += 1
    return(1)

inconvinience = N*(N-1)//2
answers=[inconvinience]

for edge in edges:
    x,y = edge
    rx = root(x)
    ry = root(y)
    sx = size[rx]
    sy = size[ry]
    res = union(rx,ry)
    if res == 1:
        inconvinience -= sx*sy
    answers.append(inconvinience)

answers.reverse()

for answer in answers[1:]:
    print(answer)