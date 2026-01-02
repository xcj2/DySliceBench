def root(nodes, x):
    if nodes[x] < 0:
        return x
    else:
        nodes[x] = root(nodes, nodes[x])
        return nodes[x]

def unite(nodes, x, y):
    root_x, root_y = root(nodes, x), root(nodes, y)
    if root_x != root_y:
        large_root = min(root_x,root_y)
        small_root = max(root_x,root_y)
        nodes[large_root] += nodes[small_root]
        nodes[small_root] = large_root 

N, M = map(int, input().split())
p = [int(e)-1 for e in input().split()]
# ノードは-1で初期化
nodes = [-1]*N
info = [[int(e)-1 for e in input().split()] for i in range(M)]
for x, y in info:
    unite(nodes, x, y)

group = [[] for i in range(N)]
for i in range(N):
    group[root(nodes,i)].append(i)

def deplications(list1,list2):
    before = len(list1) + len(list2)
    list3 = list(set(list1 + list2))
    after = len(list3)
    return before - after

def make_list(list1):
    list2 = [p[e] for e in list1]
    return list2

ans = 0
for pair in group:
    if pair == []:
        continue
    ans += deplications(pair,make_list(pair))

print(ans)