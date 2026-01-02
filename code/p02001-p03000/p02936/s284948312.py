import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


N, Q = map(int, input().split())
 
class Node():
    def __init__(self):
        self.connected = []
        self.count = 0
 
 
 
def add_count(v, p):
    for c in G[v].connected:
        if c == p:
            continue
        G[c].count += G[v].count
        add_count(c, v)

def add_count2():
    s = [(0, -1)]
    while s:
        v, p = s.pop()
        for c in G[v].connected:
            if c == p:
                continue
            G[c].count += G[v].count
            s.append((c, v))

G = [Node() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].connected.append(b-1)
    G[b-1].connected.append(a-1)

for _ in range(Q):
    p, x = map(int, input().split())
    G[p-1].count += x

# add_count(0, -1)
add_count2()
counts = [node.count for node in G]
print(*counts)

