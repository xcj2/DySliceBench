N,M = map(int, input().split())
AB = [ [int(j) for j in input().split()] for _ in range(M)]


data = [-1]*(N+1)
rank = [1]*(N+1)
con  = [1] * (N+1)
def find(a):
    while data[a] != -1:
        a = data[a]
    return a
def unite(a,b):
    a=find(a); b=find(b)
    if a != b:
        if rank[a] < rank[b]:
            b,a = a,b
        if rank[a] == rank[b]:
            rank[a] += 1
        rank[b] += rank[a]
        data[b] =  a
        con[a]  += con[b]


con = [ [] for _ in range(N+1)]

def is_edge(a):
    if len(con[a]) == 1:
        return True
    return False


conF = [ [False] * (N+1) for _ in range(N+1)]
for a,b in AB:
    # if find(a) != find(b):
    #     ans += 1
    #     unite(a,b)
    con[a].append(b)
    con[b].append(a)
    conF[a][b] = True
    conF[b][a] = True

def dfs(cnt, n, par,  target, visited):
    # print("dfs({}, {}, {}, {}, {}".format(cnt, n, par, target, visited))
    if cnt != 0 and n == target:
        return True

    found = False
    visited[n] = True
    for ch in con[n]:
        if ch == par: continue
        if visited[ch]: continue
        if not conF[ch][n] : continue

        found = dfs(cnt+1, ch, n, target, visited[:])
        if found:
            # print("\tFound!")
            break
    if found:
        return True
    else:
        return False

ans = 0
for a,b in AB:
    conF[a][b] = False
    conF[b][a] = False

    found = False
    for ch in con[a]:
        if ch == b: continue
        visited = [False] * (N+1)
        visited[a] = True
        
        found = dfs(0, ch ,a, b, visited[:])
        if found:
            break
    if not found:
        # print("a: ", a, "b: ", b, "+1! ")
        ans += 1
    # ---- 
    conF[a][b] = True
    conF[b][a] = True

print(ans)

