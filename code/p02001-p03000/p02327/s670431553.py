import sys, collections, heapq
file = sys.stdin
H,W = map(int, file.readline().split())
C = [list(map(int,i.split())) for i in file.readlines()]
prev = [0 for i in range(W)]
G = []
def height(C):
    global prev
    P = []
    for i in range(W):
        if C[-1][i] == 1:
            p = 0
        else: p = prev[i] + 1
        P.append(p)
    prev = P[:]
    return P

def square(C):
    P = height(C)
    global G
    L = collections.deque()
    for i,v in enumerate(P):
        if not L:
            L.append((i, v))
            continue
        if v > L[-1][1]:
            L.append((i, v))
        elif v < L[-1][1]:
            k = i - 1
            while L and v < L[-1][1]:
                a = L.pop()
                heapq.heappush(G,  -(k - a[0] + 1) * a[1])
            L.append((a[0], v))
    while L:
        a = L.pop()
        heapq.heappush(G, -(len(P) - a[0]) * a[1])

def ans(C):
    ans = []
    global G
    for i in range(H):
        currentC = C[:i+1]
        square(currentC)
    return str(-G[0])

print(ans(C))