N, M, K = map(int, input().split())
table = [-1]*N
def union(x, y):
    global table
    x, y = find(x), find(y)
    if x==y:
        return False
    else:
        if table[x]>table[y]:
            x, y = y, x
        table[x] += table[y]
        table[y] = x
        return True
def find(x):
    if table[x]<0:
        return x
    else:
        table[x] = find(table[x])
        return table[x]
def rank(x):
    return table[find(x)]
friend = [[] for _ in range(N)]
block = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)
    union(a-1, b-1)

for _ in range(K):
    c, d = map(int, input().split())
    block[c-1].append(d-1)
    block[d-1].append(c-1)

ans = [""]*N
for i in range(N):
    tmp = abs(rank(i)) - len(friend[i]) - 1
    cnt = 0
    for b in block[i]:
        if find(i)==find(b):
            cnt += 1
    ans[i] = str(tmp - cnt)
print(" ".join(ans))