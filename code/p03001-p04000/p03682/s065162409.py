import sys
N = int(input())
city_ls = list()
for i in range(N):
    city_ls.append([int(i) for i in sys.stdin.readline().split()])
sort_by_x = sorted([[i, j] for i,j in city_ls], key=lambda x:x[0])
G = []
pos2id = {tuple(j) : i for i, j in enumerate(city_ls)}
for i in range(len(sort_by_x)-1):
    current_by_x = sort_by_x[i]
    next_by_x = sort_by_x[i + 1]
    G.append((abs(current_by_x[0] - next_by_x[0]),current_by_x, next_by_x))
sort_by_x.sort(key=lambda x:x[1])
for i in range(len(sort_by_x) - 1):
    current_by_x = sort_by_x[i]
    next_by_x = sort_by_x[i + 1]
    G.append((abs(current_by_x[1] - next_by_x[1]), current_by_x, next_by_x))
G.sort(key=lambda x:x[0])
sum_cost = 0
par = [i for i in range(N)]
rank = [1 for i in range(N)]
def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        pass
    else:
        if rank[x] > rank[y]:
            par[y] = x
            rank[x] += rank[y]
        else:
            par[x] = par[y]
            rank[y] += rank[x]

def is_same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False

for i in G:
    (cost, _from, _to) = i
    _from = pos2id[tuple(_from)]
    _to = pos2id[tuple(_to)]
    if is_same(_from, _to):
        continue
    unite(_from, _to)
    sum_cost += cost
print(sum_cost)