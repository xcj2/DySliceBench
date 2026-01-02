label = {}
flow = {}
s, t = 'S', 'T'

def printpath(path):
    return
    for u, v in zip(path, path[1:]):
        print("%s -%d-> " % (label[u], flow[(u,v)]), end="")
    print("")

def printflow():
    return
    print("--flow--")
    for r in R:
        for b in edges[r]:
            print("  ", label[r], label[b], "s->r=%d"%flow[(s, r)], ", r->b=%d"%flow[(r, b)], ", b->t=%d"%flow[(b, t)])
            #print("  ", label[r], label[b], "r->s=%d"%flow[(r, s)], ", b->r=%d"%flow[(b, r)], ", t->b=%d"%flow[(t, b)])
        if edges[r]:
            print()

def findpath(v, t, edges, flow, visited):
    visited.add(v)
    #print(label[v], edges[v])
    for u in edges[v]:
        if u in visited:
            continue
        if flow[(v, u)] == 1:
            continue
        if u == t:
            return [v, t]
        path = findpath(u, t, edges, flow, visited)
        if path:
            return [v] + path
    return None

def max_match(R, B, edges):

    # init edge b - t
    for b in B:
        flow[(b, t)] = 0
        flow[(t, b)] = 1
        edges[b].append(t)

    edges[s] = []
    # init edge s - r
    for r in R:
        flow[(s, r)] = 0
        flow[(r, s)] = 1
        edges[s].append(r)

        # init flow r - b
        for b in edges[r]:
            flow[(r, b)] = 0
            flow[(b, r)] = 1

    change = True
    while change:
        printflow()
        change = False
        for r in R:
            if flow[(s, r)] == 1:
                continue
            path = findpath(r, t, edges, flow, set([s]))
            if not path:
                continue
            #printpath(path)
            path = [s] + path
            for u, v in zip(path, path[1:]):
                flow[(u, v)] = 1
                flow[(v, u)] = 0
            change = True
    printflow()
    return flow

def solve(R, B, edges):
    flow = max_match(R, B, edges)

    match = 0
    for r in R:
        for b in edges[r]:
            match += flow[(r, b)]
    return match
            

N = int(input())

R = [tuple([int(x) for x in input().split()]) for _ in range(N)]
B = [tuple([int(x) for x in input().split()]) for _ in range(N)]
for i, r in enumerate(R):
    label[r] = "R%d" % (i+1)
    #print(label[r], r)
for i, r in enumerate(B):
    label[r] = "B%d" % (i+1)
    #print(label[r], r)
label[s] = 'S'
label[t] = 'T'

edges = {}
for r in R:
    edges[r] = []
for b in B:
    edges[b] = []

for r in R:
    rx, ry = r
    for b in B:
        bx, by = b
        if rx < bx and ry < by:
            edges[r].append(b)
            edges[b].append(r)


print(solve(R, B, edges))


