# F - Tree and Constraints

# Read input

n = int(input())
adj = {a: [] for a in range(1, n + 1)}
for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
m = int(input())
ranges = []
for i in range(m):
    u, v = map(int, input().split())
    ranges.append((u, v))

# Subroutines

def normalized(u, v):
    return (min(u, v), max(u, v))

def findpath(u, v, visited=None):
    """uからvへの経路 (辺の集合)"""
    if visited is None:
        visited = set()
    if u == v:
        return set()
    if u in visited:
        return None
    visited.add(u)
    for x in adj[u]:
        p = findpath(x, v, visited)
        if p is not None:
            p.add(normalized(u, x))
            return p

def powerset(seq, bag):
    """(seqの部分集合s, bag[e] for e in s の和集合)"""
    if len(seq) <= 1:
        yield ((seq[0],), bag[seq[0]])
        yield ((), set())
    else:
        for s, b in powerset(seq[1:], bag):
            yield ((seq[0],) + s, b | bag[seq[0]])
            yield (s, b)

# Find paths

paths = {}
for u, v in ranges:
    paths[(u, v)] = findpath(u, v)

# いずれかの区間をすべて白にする塗り方の個数
coloring = 0
for s, b in powerset(ranges, paths):
    l = len(s)
    if l <= 0:
        continue
    # b中の辺をすべて白にする塗り方の個数
    c = 2 ** ((n - 1) - len(b))
    # 包除原理
    sign = -1 if l % 2 == 0 else 1    
    coloring += sign * c

# どの区間も黒を含む塗り方の個数
coloring = 2 ** (n - 1) - coloring
print(coloring)
