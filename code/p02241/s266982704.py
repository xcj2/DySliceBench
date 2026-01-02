N = int(input())
P = [i for i in range(N)]
weight = []

def root(x):
    path_to_root = []
    while P[x] != x:
        path_to_root.append(x)
        x = P[x]
    for node in path_to_root:
        P[node] = x
    return x

def is_same_set(x,y):
    return root(x) == root(y)

def unite(x,y):
    P[root(x)] = root(y)
    
# まずは辺の重さをソートするために辺の重さの配列を作りましょう→マイナス1は除外
for i in range(N):
    lis = list(map(int,input().split()))
    for j in range(N):
        if lis[j] == -1:
            continue
        else:
            weight.append([lis[j],i,j])
# ソートされた順に小さい順から次々とuniteして行こう
weight.sort()
length = len(weight)
k = 0
total_weight = 0

for k in range(length):
    if is_same_set(weight[k][1],weight[k][2]):
        continue
    else:
        unite(weight[k][1],weight[k][2])
        total_weight += weight[k][0]

print(total_weight)
    
# その際にもし付け加えてis_same_set(x,y)がtrueだったらやめよう

