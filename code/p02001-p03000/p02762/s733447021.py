n,q,qq=map(int,input().split())

# root番号保持
root = list(range(n))
# 階層保持
rank =  [0] * n
# ノード数
node =  [1] *n
minus_node =  [0] *n


def find_set(x):
    if(x != root[x]):
        root[x] = find_set(root[x])
    return root[x]

def unite(x,y):
    link(find_set(x),find_set(y))

def link(x,y):
    if root[x] == root[y]:return
    if rank[x] > rank[y]:
        root[y] =x
        node[x] += node[y] 
    else:
        root[x] = y
        node[y] += node[x] 
        if rank[x] == rank[y]:
            rank[y] +=1

def same(x,y):
    return find_set(x) == find_set(y)

# print(root)
# print(rank)
# print(node)


for _ in range(q):
    a,b = map(int,input().split())

    unite(a-1,b-1)
    minus_node[a-1] +=1
    minus_node[b-1] +=1
    # print()
    # print(root)
    # print(rank)
    # print(node)

for _ in range(qq):
    a,b = map(int,input().split())

    if same(a-1,b-1):
        minus_node[a-1] +=1
        minus_node[b-1] +=1
# print()
# print(root)
# print(rank)
# print(node)


print(" ".join([str(node[find_set(i)] - minus_node[i] -1) for i in range(n)]))
