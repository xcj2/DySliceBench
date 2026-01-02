E = []
v, e = map(int, input().split())
for _ in range(e):
    s, t, w = map(int, input().split())
    E.append((w, s, t))


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [-1]*N

    def findset(self, A):
        if self.parent[A] < 0:
            return A
        self.parent[A] = self.findset(self.parent[A])
        return self.parent[A]

    def size(self, A):
        return -self.parent[self.findset(A)]

    def unite(self, A, B):
        A = self.findset(A)
        B = self.findset(B)

        if A == B:
            return False

        if self.size(A) > self.size(B):
            A, B = B, A

        self.parent[A] += self.parent[B]
        self.parent[B] = A

        return True

    def is_same(self, A, B):
        return self.findset(A) == self.findset(B)
        

def kruskal(N):
    edges = sorted(E)
    ans = 0
    union = UnionFind(N)
    cnt = 0
    for w, s, t in edges:
        if cnt == N-1:
            break

        if union.is_same(s, t):
            continue
        else:
            union.unite(s, t)
            ans += w
            cnt += 1
            
    return ans

print(kruskal(v))
