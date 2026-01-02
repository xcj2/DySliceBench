from collections import deque

class Dinic:
    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]
    
    def add_edge(self, init, end, capacity):
        '''
            e[0] = the head vertex of e,
            e[1] = current capacity of e,
            e[2] = the index of reverse edge of e.
        '''
        self.E[init].append([end, capacity, len(self.E[end])])
        self.E[end].append([init, 0, len(self.E[init]) - 1])
    
    def _exist_augpath(self, s, t):
        self.level = level = [-1] * self.N # the level (depth) of each vertex
        E = self.E
        q = deque([(s, 0)]) # (vertex, level)
        while q:
            v, lv = q.popleft()
            if level[v] < 0: # visited v for the first time
                level[v] = lv
                for u, cap, _ in E[v]:
                    if cap == 0 or level[u] >= 0: continue
                    q.append((u, lv + 1))
        return level[t] >= 0
    
    def _blocking_flow(self, s, t):
        aug_flow = 0
        finished = [False] * self.N
        parent = [-1] * self.N
        revs = [-1] * self.N
        bottleneck = -1; temp_flow = 0
        E, level = self.E, self.level
        stack = [(s, -1, float('inf'), -1, 0)] # (vertex, parent, flow, rev_idx, status)
        while stack:
            v, p, f, rev, st = stack.pop()
            if temp_flow and v != bottleneck: continue
            if st == 0 and not finished[v]:
                parent[v] = p; revs[v] = rev
                if temp_flow: # offset
                    f -= temp_flow; temp_flow = 0; bottleneck = -1
                if v == t: # an augment path is found
                    aug_flow += f
                    if p != -1: stack += [(v, p, f, rev, 3)]
                    continue
                n_children = 0
                for u, cap, rev_idx in E[v]:
                    if cap == 0 or finished[u] or level[u] != level[v] + 1: continue
                    if n_children == 0:
                        stack += [(v, p, 0, rev, 2), (u, v, min(f, cap), rev_idx, 0)]
                        n_children += 1
                    else:
                        stack += [(v, p, 0, rev, 1), (u, v, min(f, cap), rev_idx, 0)]
                        n_children += 1
                if n_children == 0: # v is a leaf
                    finished[v] = True
            elif st == 1: # now searching
                continue
            elif st == 2: # search finished
                finished[v] = True
            else: # edge update
                rev_e = E[v][rev]; e = E[p][rev_e[2]]
                e[1] -= f; rev_e[1] += f
                if e[1] == 0: bottleneck = p
                if parent[p] != -1: stack += [(p, parent[p], f, revs[p], 3)]
                else: temp_flow = f
        return aug_flow
    
    def max_flow(self, s, t):
        flow = 0
        exist_augpath, blocking_flow = self._exist_augpath, self._blocking_flow
        while True:
            if not exist_augpath(s, t): break # no augment path is found
            flow += blocking_flow(s, t)
        return flow

N, M = map(int, input().split())
di = Dinic(N)
for _ in range(M):
    u, v, c = map(int, input().split())
    di.add_edge(u, v, c)
print(di.max_flow(0, N-1))
