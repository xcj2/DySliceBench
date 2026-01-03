class PreallocatedQueue:
    def __init__(self, n, init_val):
        self.queue = [init_val] * n #根にサイズを負の値で格納する。
        self.l = 0
        self.r = 0
        self.n = n
        self.init_val = init_val
        self.count = 0

    def append(self, val):
        if self.count == self.n:
            if self.r == 0:
                self.queue = self.queue + [self.init_val] * self.n
            else:
                self.queue = self.queue[self.l:] + self.queue[:self.r] + [self.init_val] * self.n
                self.l = 0
            self.r = self.n
            self.n *= 2
        self.queue[self.r] = val
        self.r = (self.r + 1) % self.n
        self.count += 1

    def popleft(self):
        if self.count == 0:
            raise IndexError('popleft from empty queue')
        val = self.queue[self.l]
        self.l = (self.l + 1) % self.n
        self.count -= 1
        return val

    def pop(self):
        if self.count == 0:
            raise IndexError('pop from empty queue')
        val = self.queue[self.r - 1]
        self.r = (self.r - 1) % self.n
        self.count -= 1
        return val
    
    def size(self):
        return self.count
    
    def __bool__(self):
        return self.count != 0

def fast_bellman_ford(n, s, graph, edge_n, init_val): #どう？
    d = [init_val] * n
    d[s] = 0
    q = PreallocatedQueue(edge_n, 0)
    q.append(s)
    checker = [-1] * n
    for i in range(n):
        m = q.count
        for _ in range(m):
            vf = q.popleft()
            for vt, w in graph[vf]:
                if d[vt] > d[vf] + w:
                    d[vt] = d[vf] + w
                    if checker[vt] < i:
                        q.append(vt)
                        checker[vt] = i
        if not q:
            break
    if q: #閉路の存在
        minus_inf = -float('inf')
        i += 1
        while q:
            m = q.count
            for _ in range(m):
                vf = q.popleft()
                for vt, w in graph[vf]:
                    if d[vt] > d[vf] + w:
                        d[vt] = minus_inf
                        if checker[vt] < i:
                            q.append(vt)
                            checker[vt] = i
            i += 1
    return d

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, -w))
d = fast_bellman_ford(n, 0, graph, 2 * m, float('inf'))
print(-d[-1] if d[-1] != -float('inf') else 'inf')
