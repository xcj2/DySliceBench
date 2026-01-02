import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

class UnionFieldTree(object):
    def __init__(self, n):
        '''1-indexed'''
        self.parent = [i for i in range(n+1)] 
        self.size = [0] + [1] * n

    def merge(self, a, b):
        '''merge b into a'''
        a = self.root(a)
        b = self.root(b)
        self.parent[b] = self.parent[a]
        self.size[a] += self.size[b]

    def root(self, a):
        parent = self.parent[a]
        if parent == a:
            return a
        r = self.root(parent)
        self.parent[a] = r
        return r
    
    def same_group(self, a, b):
        return self.root(a) == self.root(b)


def main():
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]
    
    uf = UnionFieldTree(N)

    v_sum = N*(N-1)//2
    ans = [v_sum]

    for a, b in reversed(AB):
        if not uf.same_group(a, b):
            ra = uf.root(a)
            rb = uf.root(b)
            v_sum -= uf.size[ra] * uf.size[rb]
            uf.merge(a, b)
        ans.append(v_sum)

    [print(a) for a in reversed(ans[:M])]


main()


