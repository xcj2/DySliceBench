N,e = map(int, input().split())
inf = float("inf")
adj = [[inf for _ in range(N)]  for _ in range(N)]
for _ in range(e):
    s,t,d = map(int, input().split())
    adj[s][t] = d

def memorize(f):
    cache = {}
    def func(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return func

@memorize
def tsp(v, b):
    if b == (1 << N) - 1:
        return adj[v][0]
    res = inf
    for w in range(N):
        if b & (1 << w): continue
        res = min(res, adj[v][w] + tsp(w, b | (1 << w)))
    return res

if tsp(0,1) == inf:
    print(-1)
else: print(tsp(0,1))