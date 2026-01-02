from heapq import heappush, heappop

def dijkstra(s, edge):
    '''
    始点sから各頂点への最短距離を求める
    '''
    d = [float("inf")] * n
    d[s] = 0
    used = [False] * n
    used[s] = True
    edgelist = []

    for e in edge[s]:
        heappush(edgelist, e)

    while edgelist:
        cost, v = heappop(edgelist)
        if used[v]:
            continue
        d[v] = cost
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heappush(edgelist, [e[0] + d[v], e[1]])

    return d


def segfunc(x, y):
    '''
    問題に応じて返り値を設定
    '''
    return min(x, y)


def init(a):
    '''
    配列aで初期化
    '''
    for i in range(n):
        seg[i+num-1] = a[i]    
    for i in range(num-2, -1, -1) :
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])


def update(k, x):
    '''
    a[k]の値をxに更新
    '''
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = segfunc(seg[k*2+1], seg[k*2+2])


def query(p, q):
    '''
    [p, q)についてsegfuncを適用したものを返す
    '''
    if q <= p:
        return ide_ele
    
    p += num - 1
    q += num - 2
    res = ide_ele

    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(res, segfunc(seg[p], seg[q]))
    
    return res


n, m, s, t = map(int, input().split())

e1 = [[] for _ in range(n)]
e2 = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    e1[u-1].append([a, v-1])
    e1[v-1].append([a, u-1])
    e2[u-1].append([b, v-1])
    e2[v-1].append([b, u-1])

d1 = dijkstra(s-1, e1)
d2 = dijkstra(t-1, e2)
dist = [d1[i] + d2[i] for i in range(n)]

num = (2 ** len(bin(n - 1)) - 2)
ide_ele = float('inf')
seg = [ide_ele] * 2 * num
init(dist)

for i in range(n):
    print(10 ** 15 - query(i, n))