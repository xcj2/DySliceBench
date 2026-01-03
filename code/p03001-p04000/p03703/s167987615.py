from bisect import bisect_left

N, K = map(int, input().split())
a = [int(input()) - K for _ in range(N)]

s = [0]
for i in range(N) :
    s.append(s[-1] + a[i])

t = list(set(s))
t.sort()
for i in range(N + 1) :
    s[i] = bisect_left(t, s[i])

class BinaryIndexedTree() :
    def __init__(self, N) :
        self.size = N
        self.tree = [0] * (N + 1)
        
    def sum(self, i) :
        s = 0
        while i > 0 :
            s += self.tree[i]
            i -= i & -i
        return s
        
    def add(self, i, x) :
        while i <= self.size :
            self.tree[i] += x
            i += i & -i
            
ret = 0
BIT = BinaryIndexedTree(N + 5)
for i in range(N + 1) :
    ret += BIT.sum(s[i] + 1)
    BIT.add(s[i] + 1, 1)
    
print(ret)