from collections import deque
n = int(input())
Ps = list(map(lambda x: int(x)-1, input().split()))
cost = [min(i, n-1-i, j, n-1-j) for i in range(n) for j in range(n)]
exist = [1]*(n**2)


def to_idx(p):
    return divmod(p, n)


def to_v(i, j):
    return i*n+j


def bfs(init_v):
    next_v = deque([init_v])
    exist[init_v] = 0
    while next_v:
        v = next_v.popleft()
        i, j = to_idx(v)
        if 0 < i:
            v2 = v-n
            if cost[v2] > cost[v]+exist[v]:
                cost[v2] = cost[v]+exist[v]
                next_v.append(v2)

        if i < n-1:
            v2 = v+n
            if cost[v2] > cost[v]+exist[v]:
                cost[v2] = cost[v]+exist[v]
                next_v.append(v2)

        if 0 < j:
            v2 = v-1
            if cost[v2] > cost[v]+exist[v]:
                cost[v2] = cost[v]+exist[v]
                next_v.append(v2)

        if j < n-1:
            v2 = v+1
            if cost[v2] > cost[v]+exist[v]:
                cost[v2] = cost[v]+exist[v]
                next_v.append(v2)

ans = 0
for p in Ps:
    ans += cost[p]
    bfs(p)
print(ans)