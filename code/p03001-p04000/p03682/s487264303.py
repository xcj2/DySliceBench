N = int(input())
h = [list(map(int, input().split())) for _ in range(N)]

x = [(val[0],i) for i,val in enumerate(h)]
y = [(val[1],i) for i,val in enumerate(h)]

x.sort()
y.sort()
edge = []
for i in range(1,N):
    # (cost, start, end)
    edge.append((x[i][0]-x[i-1][0], x[i-1][1], x[i][1]))
    edge.append((y[i][0]-y[i-1][0], y[i-1][1], y[i][1]))
edge.sort()
par = list(range(N))
rank = [0]*N

def find(val):
    if par[val]==val:
        return val
    else:
        par[val] = find(par[val])
        return par[val]

def unite(val1, val2):
    val1 = find(val1)
    val2 = find(val2)
    if val1==val2:
        return
    if rank[val1] < rank[val2]:
        par[val1] = val2
    else:
        par[val2] = val1
        if rank[val1] == rank[val2]:
            rank[val1] += 1
def same(val1, val2):
    return find(val1)==find(val2)

res = 0
for e in edge:
    start = e[1]
    end = e[2]
    if same(start, end):
        continue
    res += e[0]
    unite(start, end)
print(res)




