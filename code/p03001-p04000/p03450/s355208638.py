class PotentializedUnionFind():
    "Either 0-indexed or 1-indexed"

    __slots__ = ["parent", "potential_diff"]

    def __init__(self, size):
        self.parent = [-1] * (size + 1)
        self.potential_diff = [0] * (size + 1) # potential_diff[node] = potential[parent[node]] - potential[node]
    
    def find(self, a):
        path = []
        while self.parent[a] > 0:
            path.append(a)
            a = self.parent[a]
        for child in reversed(path):
            self.potential_diff[child] += self.potential_diff[self.parent[child]]
            self.parent[child] = a
        return a

    def union(self, a, b, diff):
        """
        connect a and b, where potential of these satisfy `potential[b] - potential[a] == diff`,
        Returning `not same(a, b)`. 
        
        If a and b are already in the same tree, then this does nothing.
        """

        a_root = self.find(a)
        b_root = self.find(b)
        diff += self.potential_diff[b] - self.potential_diff[a] # find で経路圧縮しているのでこれでよい。
        a = a_root
        b = b_root

        if a == b:
            return False 
        else:
            if self.parent[a] == self.parent[b]:
                self.parent[a] = b
                self.parent[b] -= 1
                self.potential_diff[a] = diff
            elif self.parent[a] < self.parent[b]: #aのほうが大きい
                self.parent[b] = a
                self.potential_diff[b] = -diff
            else:
                self.parent[a] = b #bのほうが大きい
                self.potential_diff[a] = diff
            return True
        
    def same(self, a, b):
        return self.find(a) == self.find(b)

    def diff(self, a, b):
        assert self.find(a) == self.find(b) # find(a) と find(b) 内での経路圧縮が本質なので、コメントアウトしない。
        return self.potential_diff[a] - self.potential_diff[b]


def main():
    import sys
    input = sys.stdin.buffer.readline
    
    N, M = map(int, input().split())
    lrds = list(map(int, sys.stdin.buffer.read().split()))
    puf = PotentializedUnionFind(N)
    ls = lrds[::3]
    rs = lrds[1::3]
    ds = lrds[2::3]
    for l, r, d in zip(ls, rs, ds):
        if not puf.union(l, r, d):
            if not puf.diff(l, r) == d:
                print("No")
                exit()
    
    print("Yes")
    
if __name__ == "__main__":
    main()