import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n,m = map(int, input().split())
ns = defaultdict(set)
es = set()
for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)
    es.add((u,v))

### サイクル検出 cycle detection

seen = [False] * n
done = [False] * n
hist = []
def dfs(u, pos):
    # uからdfs
    seen[u] = True
    hist.append(u)
    for v in ns[u]:
        if done[v]:
            continue
        elif seen[v]:
            # サイクルを検出
            pos = v
            return pos
        else:
            pos = dfs(v, pos)
            if pos>=0:
                return pos
    done[u] = True
    hist.pop()
    return pos

# サイクル復元
def cycle(hist, pos):
    for i, u in enumerate(hist):
        if u==pos:
            break
    return hist[i:]
# 極小サイクルを復元
def sub(hist):
    s = set(hist)
    ss = set((hist[i],hist[i+1]) for i in range(len(hist)-1))
    ss.add((hist[len(hist)-1], hist[0]))
    l = None
    for u,v in es:
        if u in s and v in s and (u,v) not in ss:
            l = []
            for i,k in enumerate(hist):
                if k==v:
                    break
            for j in range(i,len(hist)):
                l.append(hist[j])
                if hist[j]==u:
                    break
            else:
                for j in range(len(hist)):
                    l.append(hist[j])
                    if hist[j]==u:
                        break
#     print(hist, l, i, u,v,ss)
    if l is None or len(l)==len(hist):
        return hist
    else:
        return sub(l)
ans = None
for u in range(n):
    pos = dfs(u, -1)
    if pos>=0:
        hist = cycle(hist, pos)
        ans = sub(hist)
        break
if ans is None:
    print(-1)
else:
    print(len(ans))
    write("\n".join(map(lambda x: str(x+1), ans)))