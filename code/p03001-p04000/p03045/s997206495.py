import math
from functools import reduce

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,m = get_nums_l()

groups = n
node_groups = [ i for i in range(n)]
group_sizes = [ 1 for _ in range(n)]
group_ranks = [ 0 for _ in range(n)]

edges = []
for i in range(m):
    tmp=input().split(" ")
    edges.append([int(tmp[0])-1, int(tmp[1])-1])


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
    global groups

    a = root(a)
    b = root(b)

    if a == b:
        return
    
    # 合体したらグループ数が減る
    groups -= 1

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

    unite(root_1, root_2)
print(groups)