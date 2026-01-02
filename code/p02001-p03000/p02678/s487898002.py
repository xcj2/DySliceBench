from collections import defaultdict as dd

def ri():
    return int(input())

def rl():
    return map(int, input().split())

def rl2():
    return list(rl())

N, M = rl()
edges = dd(list)
for i in range(M):
    A, B = rl()
    edges[A].append(B)
    edges[B].append(A)

parents = {1:0}
ring = [1]
while ring:
    nxt = []
    for room in ring:
        for nbr in edges[room]:
            if nbr not in parents:
                parents[nbr] = room
                nxt.append(nbr)
    ring = nxt

if len(parents) < N:
    print ("No")
else:
    print ("Yes")
    for i in range(2, N + 1):
        print (parents[i])

