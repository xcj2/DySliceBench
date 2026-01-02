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
    print(len([list(x) for x in gen]))

n,m=map(int,input().split())
d={i:[] for i in range(n)}
for i in range(m):
    x,y,z=map(int,input().split())
    d[x-1].append(y-1)
    d[y-1].append(x-1)

print_gen(connected_components(d))