class Tree:
    def __init__(self, v: int):
        self.value = v
        self.size = 1
        self.depth = 1
        self.parent = None
        self.friends = set()
        self.blocked = 0

    def get_root(self):
        t = self
        while(t.parent != None):
            t = t.parent
        return t

    def merge(self, t):
        p, c = (self, t) if self.depth > t.depth else (t, self)
        c.parent = p
        p.depth = max(p.size, c.size + 1)
        p.size += c.size

def main():
    n, m, k = [int(s) for s in input().split()]
    forest = [Tree(i+1) for i in range(n)]

    for i in range(m):
        a, b = [int(s) for s in input().split()]
        ta, tb = forest[a-1], forest[b-1]
        ta.friends.add(b)
        tb.friends.add(a)
        ra = ta.get_root()
        rb = tb.get_root()
        if ra != rb:
            ra.merge(rb)

    roots = [t.get_root() for t in forest]
    for i in range(k):
        c, d = [int(s) for s in input().split()]
        tc, td = forest[c-1], forest[d-1]
        rc = roots[c-1]
        rd = roots[d-1]
        if rc == rd:
            tc.blocked +=1
            td.blocked +=1

    cands = []
    for t in forest:
        root = roots[t.value - 1]
        cand = root.size - len(t.friends) - t.blocked - 1
        cands.append(str(cand))
    print(" ".join(cands))

if __name__ == '__main__':
    main()
