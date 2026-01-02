H, W = map(int, input().split())
S = [input() for _ in range(H)]

import heapq
def dijkstra(adj, n, st=1):
    dj = [2**64] * (n)
    dj[st] = 0
    q = []
    heapq.heappush(q, (0, st))
    while q:
        fc, fn = heapq.heappop(q)
        if dj[fn] < fc: continue
        for tn, lc in adj[fn]:
            if dj[fn] + lc < dj[tn]:
                dj[tn] = dj[fn] + lc
                heapq.heappush(q, (dj[tn], tn))
    return dj

def cid(x):
    return x[0] * W + x[1]

def cl(adj, x, y):
    xid = cid(x)
    yid = cid(y)
    adj[xid].append((yid, 1))
    adj[yid].append((xid, 1))

adj = dict([(x, []) for x in range(H*W)])
for i in range(H):
    for j in range(W):
        if S[i][j] == "#": continue
        ni = i + 1
        if ni < H and S[ni][j] == ".":
            cl(adj, (i, j), (ni, j))
        nj = j + 1
        if nj < W and S[i][nj] == ".":
            cl(adj, (i, j), (i, nj))

c = dijkstra(adj, H*W, cid((0,0)))
hwc = c[cid((H-1,W-1))]
print(-1 if hwc == 2**64 else H * W - sum(s.count("#") for s in S) - hwc - 1)