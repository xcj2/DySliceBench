import collections,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
n = I()
ukv = [LI() for _ in range(n)]
graph = {i:collections.deque() for i in range(1,n+1)} #1_indexed
for x in ukv:
    u,k,*v = x
    for y in v:
        graph[u].append(y)
seen = [0]*(n+1) #1_indexed
stack = []
time = 0
seentime = [0]*(n+1) #1_indexed
donetime = [0]*(n+1) #1_indexed
def dfs(j):
    global time
    seen[j] = 1
    stack.append(j)
    time += 1
    seentime[j] = time
    while stack:
        s = stack[-1]
        if not graph[s]:
            stack.pop()
            time += 1
            donetime[s] = time
            continue
        g_NO = graph[s].popleft()
        if seen[g_NO]:
            continue
        seen[g_NO] = 1
        stack.append(g_NO)
        time += 1
        seentime[g_NO] = time
for j in range(1,n+1):
    if seen[j]:
        continue
    dfs(j)
for k,a,b in zip(range(1,n+1),seentime[1:],donetime[1:]):
    print(k,a,b)
