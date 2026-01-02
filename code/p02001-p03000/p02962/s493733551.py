s = input()
t = input()

def Z(S):
    A = [0]*len(S)
    i = 1; j = 0
    A[0] = len(S)
    while i < len(S):
        while i+j < len(S) and S[j] == S[i+j]:
            j += 1
        A[i] = j
        if not j:
            i += 1
            continue
        k = 1
        while len(S)-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

z = Z(t+'?'+s*(len(t)//len(s)+2))
z = z[len(t)+1:]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return 

        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y

            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def card(self, x):
        return -self.root[self.find(x)]

u = UnionFind(len(s))

for i in range(len(s)):
    if z[i] == len(t):
        if u.same(i,(i+len(t))%len(s)):
            print(-1)
            exit()
        u.unite(i,(i+len(t))%len(s))


print(-1+max(map(lambda x:-x,u.root)))
