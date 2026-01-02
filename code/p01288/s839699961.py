class UnionFind:
    def __init__(self, size):
        self.table = [None] * size

    def find(self, x):
        if self.table[x] == None:
            return x
        else:
            # compression of the path
            self.table[x] = self.find(self.table[x])
            return self.table[x]
    
    def union(self, parent, child):
        p_root = self.find(parent)
        c_root = self.find(child)
        if p_root != c_root:
            self.table[c_root] = p_root
        
def solve():
    import sys
    input_lines = sys.stdin.readlines()
    while True:
        N, Q = map(int, input_lines[0].split())
        if N == 0:
            break
        
        parent = [0, 1] + list(map(int, input_lines[1:N]))
        
        unmarked = [True] * (N + 1)
        unmarked[1] = False
        operation = []
        for o in input_lines[N:N+Q]:
            mq, v = o.split()
            v = int(v)
            if mq == 'M':
                if unmarked[v]:
                    unmarked[v] = False
                    operation.append((mq, v))
            else:
                operation.append((mq, v))
        
        uf = UnionFind(N + 1)
        for v, p in enumerate(parent[2:], start=2):
            if unmarked[v]:
                uf.union(p, v)
        
        ans = 0
        for mq, v in reversed(operation):
            if mq == 'M':
                uf.union(parent[v], v)
            else:
                ans += uf.find(v)
        
        print(ans)
        
        del input_lines[:N+Q]

solve()
