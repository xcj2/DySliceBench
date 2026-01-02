# import sys

# sys.setrecursionlimit(2000)

tmp=input().split(" ")
n = int(tmp[0])
m = int(tmp[1])

node_groups = [ i for i in range(n)]
group_sizes = [ 1 for _ in range(n)]
group_ranks = [ 0 for _ in range(n)]

edges = []
for i in range(m):
    tmp=input().split(" ")
    edges.append([int(tmp[0])-1, int(tmp[1])-1])

hubensa_list = [0] * (m + 1)
hubensa_list[m] = n*(n-1)//2

def root(i):
    if node_groups[i] == i:
        #print(i, "is root.")
        return i
    else:
        #_1 = node_groups[i]
        node_groups[i] = root(node_groups[i])
        #_2 = node_groups[i]
        #print ("root: ", _1, _2)
        return node_groups[i]

def same(a, b):
    return root(a) == root(b)

def size(i):
    return group_sizes[root(i)]

def unite(a, b):
    a = root(a)
    b = root(b)

    if a == b:
        return

    if group_ranks[a] < group_ranks[b]:
        group_sizes[b] += size(a)
        node_groups[a] = b
    else:
        group_sizes[a] += size(b)
        node_groups[b] = a
        if group_ranks[a] == group_ranks[b]:
            group_ranks[a] += 1


for i in range(m-1, -1, -1):
    edge = edges[i]
    # print("edge: ",edge)
    #print("node_groups: ", node_groups)
    node_1 = edge[0]
    node_2 = edge[1]

    root_1 = root(node_1)
    root_2 = root(node_2)
    if root_1 == root_2:
        hubensa_list[i] = hubensa_list[i+1]
        continue

    # 不便さをだす
    hubensa_list[i] = hubensa_list[i+1] - (size(root_1) * size(root_2))

    unite(root_1, root_2)

#print("node_groups: ", node_groups)


for i in range(1, m+1):
    print(hubensa_list[i])