class UnionFindTree:
    def __init__(self, a_elements):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        class ZeroDict(dict):
            def __missing__(self, key):
                self[key] = 0
                return 0 

        class OneDict(dict):
            def __missing__(self, key):
                self[key] = 1 
                return 1 
        self.parents = KeyDict()
        self.ranks = ZeroDict()
        self.sizes = OneDict()

        if a_elements is not None:
            for e in a_elements:
                _ = self.parents[e]
                _ = self.ranks[e]

    def find_root(self, a_x):
        if self.parents[a_x] == a_x:
            return a_x

        self.parents[a_x] = self.find_root(self.parents[a_x])
        return self.parents[a_x]

    def unite(self, a_x, a_y):
        rx = self.find_root(a_x)
        ry = self.find_root(a_y)
        if rx == ry:
            return

        if self.ranks[rx] < self.ranks[ry]:
            self.parents[rx] = ry
            self.sizes[ry] = self.sizes[ry] + self.sizes[rx]
        else:
            self.parents[ry] = rx
            self.sizes[rx] = self.sizes[rx] + self.sizes[ry]
            if self.ranks[rx] == self.ranks[ry]:
                # find_root makes the depth of tree whose root is ry one
                # +1 indicates child ry
                self.ranks[rx] = self.ranks[rx] + 1
    
    def is_same(self, a_x, a_y):
        return self.find_root(a_x) == self.find_root(a_y)

N, M = [int(e) for e in input().split(" ")]
uft = UnionFindTree([i for i in range(1, N+1)])
ABs = []
for _ in range(M):
    ABs.append([int(e) for e in input().split(" ")])
maxValue = N * (N-1) // 2
ans = [maxValue]
flagSkip = False
for i in range(M-1):
    a, b = ABs[M-1-i]
    if flagSkip is True:
        ans.append(0)
        continue
    
    ra = uft.find_root(a)
    rb = uft.find_root(b)
    delta = 0
    if ra != rb:
        size_a = uft.sizes[ra]
        size_b = uft.sizes[rb]
        delta = size_a * size_b
        uft.unite(a, b)
    
    d = ans[-1] - delta
    ans.append(d)
    if d == 0:
        flagSkip = True

txt = "\n".join(map(str, reversed(ans)))
print(txt)
