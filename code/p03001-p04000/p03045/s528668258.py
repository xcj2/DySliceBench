n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(m)]
g = {}
for i in range(1,n+1):
    g[i] = []
for x,y,z in l:
    g[x].append(y)
    g[y].append(x)

def connected_components(graph):
    seen = set()
    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)

def print_gen(gen):
    a = [list(x) for x in gen]
    print(len(a))

print_gen(connected_components(g))