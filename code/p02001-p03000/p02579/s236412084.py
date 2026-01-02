from collections import Counter, defaultdict, deque

R, C = [int(x) for x in input().split()]
source = tuple([int(x) - 1 for x in input().split()])  # 0 indexed
dest = tuple([int(x) - 1 for x in input().split()])  # 0 indexed
grid = [input() for r in range(R)]


drdc = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def getNbrGrid(node):
    r, c = node
    for dr, dc in drdc:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            yield nr, nc



def bfs(source, getNbr):
    q = deque([source])
    dist = {source: 0}
    while q:
        node = q.popleft()
        d = dist[node]
        for nbr in getNbr(node):
            if nbr not in dist:
                q.append(nbr)
                dist[nbr] = d + 1
    return dist


numComps = 0
compId = {}
for r in range(R):
    for c in range(C):
        if grid[r][c] != "#" and (r, c) not in compId:
            dist = bfs((r, c), getNbrGrid)
            for node in dist:
                compId[node] = numComps
            numComps += 1

if False:
    for r in range(R):
        for c in range(C):
            print(str(compId.get((r, c), ' ')).rjust(3), end="")
        print()

graph = defaultdict(set)
for r in range(R):
    for c in range(C):
        if grid[r][c] != '#':
            comp1 = compId[(r, c)]
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                        comp2 = compId[(nr, nc)]
                        graph[comp1].add(comp2)

def getNbrComp(node):
    return graph[node]


if source not in compId or dest not in compId:
    print(-1)
    exit()
sourceComp = compId[source]
destComp = compId[dest]
dist = bfs(sourceComp, getNbrComp)
if destComp not in dist:
    print(-1)
    exit()
print(dist[destComp])