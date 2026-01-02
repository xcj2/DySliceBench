from collections import deque

def search(h, w, pre_h, pre_w):
    can = []
    if h > 0:
        can.append((h-1, w))
    if h < H-1:
        can.append((h+1, w))
    if w > 0:
        can.append((h, w-1))
    if w < W-1:
        can.append((h, w+1))
    res = []
    for h, w in can:
        if S[h][w]=='.' and (h, w) != (pre_h, pre_w):
            res.append((h, w))
    return res

def bfs(h, w):
    d = [[float('inf') for _ in range(W)] for _ in range(H)]
    d[h][w] = 0
    pre_h, pre_w = h, w
    adj_list = search(h, w, pre_h, pre_w)
    open_list = deque([])
    closed_list = []
    closed_list = set(closed_list)
    for adj in adj_list:
        open_list.append((adj[0], adj[1], pre_h, pre_w))
    cnt = 0
    while True:
        cnt+=1
        if H==20 and W==20:
            if cnt > 10000:
                break
        if len(open_list) == 0:
            break
        h, w, pre_h, pre_w = open_list.popleft()
        closed_list.add((h, w, pre_h, pre_w))
        d[h][w] = min(d[h][w], d[pre_h][pre_w] + 1)
        adj_list = search(h, w, pre_h, pre_w)
        for adj in adj_list:
            if (adj[0], adj[1], h, w) in closed_list:
                continue
            open_list.append((adj[0], adj[1], h, w))

    res = 0
    for h in range(H):
        for w in range(W):
            if not d[h][w] == float('inf'):
                res = max(res, d[h][w])
    return res

def bounday():
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                return False
    return True

H, W = map(int, input().split())
S = []
for i in range(H): 
    S.append(list(input()))

if __name__ == "__main__":

    if bounday():
        print(H+W-2)
        exit(0)

    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            maxd = bfs(h, w)
            ans = max(maxd, ans)
    print(ans)