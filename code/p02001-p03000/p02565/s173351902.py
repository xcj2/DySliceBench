import sys

input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,d = list(map(int, input().split()))
xy = [tuple(map(int, input().split())) for _ in range(n)]
class SAT2:
    def __init__(self, n):
        self.n = n
        self.ns = [[] for _ in range(2*n)]
    def add_clause(self, i, f, j, g):
        """(xi==f) and (xj==g)
        """
        n = self.n
        u0,u1 = (i,i+n) if f else (i+n,i)
        v0,v1 = (j,j+n) if g else (j+n,j)
        self.ns[u1].append(v0)
        self.ns[v1].append(u0)
    def solve(self):
        """強連結成分分解
        トポロジカルソート順の逆順に返す
        """
        preorder = {}
        lowlink = {}
        seen = [False]*(2*self.n)
        scc_queue = []
        i = 0  # Preorder counter
        # ans = [None]*(2*self.n)
        count = 1
        for source in range(2*self.n):
            if seen[source]:
                continue
            queue = [source]
            while queue:
                v = queue[-1]
                if v not in preorder:
                    i = i + 1
                    preorder[v] = i
                done = True
                for w in self.ns[v]:
                    if w not in preorder:
                        queue.append(w)
                        done = False
                        break
                if done:
                    lowlink[v] = preorder[v]
                    for w in self.ns[v]:
                        if seen[w]:
                            continue
                        if preorder[w] > preorder[v]:
                            lowlink[v] = min([lowlink[v], lowlink[w]])
                        else:
                            lowlink[v] = min([lowlink[v], preorder[w]])
                    queue.pop()
                    if lowlink[v] == preorder[v]:
                        scc = {v}
                        while scc_queue and preorder[scc_queue[-1]] > preorder[v]:
                            k = scc_queue.pop()
                            scc.add(k)
                        for v in scc:
                            seen[v] = count
                        count += 1
                    else:
                        scc_queue.append(v)
        ans = [None]*self.n
        for i in range(self.n):
            if seen[i]==seen[i+self.n]:
                return None
            elif seen[i]>seen[i+self.n]:
                # 上流にxがある: x-> not x : x==False
                ans[i] = False
            else:
                ans[i] = True
        return ans

solver = SAT2(n)
for i in range(n):
    for j in range(i+1,n):
        if abs(xy[i][0]-xy[j][0])<d:
            solver.add_clause(i,False,j,False)
        if abs(xy[i][0]-xy[j][1])<d:
            solver.add_clause(i,False,j,True)
        if abs(xy[i][1]-xy[j][0])<d:
            solver.add_clause(i,True,j,False)
        if abs(xy[i][1]-xy[j][1])<d:
            solver.add_clause(i,True,j,True)
ans = solver.solve()
if ans is not None:
    print("Yes")
    write("\n".join(map(str, [xy[i][0 if ans[i] else 1] for i in range(n)])))
else:
    print("No")