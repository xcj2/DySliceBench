
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

##* graph
##pre graph
m,lst,nxt,to=0,[],[],[]

def init_graph(node_count, edge_count):
    global lst,nxt,to
    lst = [-1 for _ in range(node_count)]
    nxt = [0  for _ in range(edge_count)]
    to  = [0  for _ in range(edge_count)]

# bidirection
def add_edge(u, v):
    global m
    nxt[m], lst[u], to[m], m = lst[u], m, v, m + 1
    nxt[m], lst[v], to[m], m = lst[v], m, u, m + 1

# bidirection weight
def add_edge(u, v, w):
    global m
    nxt[m], lst[u], to[m], m = lst[u], m, (v, w), m + 1
    nxt[m], lst[v], to[m], m = lst[v], m, (u, w), m + 1

def traverse(u):
    m = lst[u]
    while m != -1:
        yield m
        m = nxt[m]


n = getint()
init_graph(n, 2 * n)

for _ in range(n - 1):
    u, v, w = getints()
    add_edge(u - 1, v - 1, w)

def get_distance(u, dist):
    dist[u] = 0
    stk = [(u, 0)]
    while stk:
        v, d = stk[-1]
        stk.pop()
        for m in traverse(v):
            vv, w = to[m]
            if dist[vv] >= 0:
                continue
            dist[vv] = d + w
            stk.append((vv, d + w))


dist = [-1]*n
get_distance(0, dist)

# print(dist)


for i in range(n):
    print(dist[i] % 2)