import sys
readline = sys.stdin.readline


class two_sat:
    def __init__(self, N):
        self.N = N
        self.Edge = [[] for _ in range(N*2)]
    
    def add_edge(self, t1, p1, t2, p2):
        # (not if t1 == 0) p1 ==> (not if t2 == 0) p2
        self.Edge[(1-t1)*self.N + p1].append((1-t2)*self.N + p2)
        
    def solve(self):
        N = len(self.Edge)
        Edgeinv = [[] for _ in range(N)]
        for vn in range(N):
            for vf in self.Edge[vn]:
                Edgeinv[vf].append(vn)
        
        used = [False]*N
        dim = [len(self.Edge[i]) for i in range(N)]
        order = []
        for st in range(N):
            if not used[st]:
                stack = [st, 0]
                while stack:
                    vn, i = stack[-2], stack[-1]   
                    if not i and used[vn]:
                        stack.pop()
                        stack.pop()
                    else:
                        used[vn] = True
                        if i < dim[vn]:
                            stack[-1] += 1
                            stack.append(self.Edge[vn][i])
                            stack.append(0)
                        else:
                            stack.pop()
                            order.append(stack.pop())
        res = [None]*N
        used = [False]*N
        cnt = -1
        for st in order[::-1]:
            if not used[st]:
                cnt += 1
                stack = [st]
                res[st] = cnt
                used[st] = True
                while stack:
                    vn = stack.pop()
                    for vf in Edgeinv[vn]:
                        if not used[vf]:
                            used[vf] = True
                            res[vf] = cnt
                            stack.append(vf)
        M = cnt+1
        components = [[] for _ in range(M)]
        for i in range(N):
            components[res[i]].append(i)
        
        for i in range(self.N):
            if res[i] == res[self.N+i]:
                return -1
        
        used = [False]*self.N
        TF = [None]*self.N
        for c in components:
            for ci in c:
                cin = ci % self.N
                if used[cin]:
                    continue
                if ci != cin:
                    TF[cin] = True
                else:
                    TF[cin] = False
                used[cin] = True  
        return TF
                
        
    
    
N, D = map(int, readline().split())

TS = two_sat(2*N)
for i in range(N):
    TS.add_edge(0, i, 1, N+i)
    TS.add_edge(0, N+i, 1, i)

Flags = [tuple(map(int, readline().split())) for _ in range(N)]

for i in range(N):
    x, y = Flags[i]
    for j in range(N):
        if i == j:
            continue
        u, v = Flags[j]
        if abs(x-u) < D:
            TS.add_edge(1, i, 0, j)
        if abs(x-v) < D:
            TS.add_edge(1, i, 0, N+j)
        if abs(y-u) < D:
            TS.add_edge(1, N+i, 0, j)
        if abs(y-v) < D:
            TS.add_edge(1, N+i, 0, N+j)

A = TS.solve()
Ans = [None]*N
if A != -1:
    print('Yes')
    for i in range(N):
        if A[i]:
            Ans[i] = Flags[i][0]
        else:
            Ans[i] = Flags[i][1]
    print('\n'.join(map(str, Ans)))
else:
    print('No')


