import sys
readline = sys.stdin.readline
      
class BIT:
    #1-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.p = 2**(n.bit_length() - 1)
        self.dep = n.bit_length()
    def get(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def bl(self, v):
        if v <= 0:
            return -1
        s = 0
        k = self.p
        for _ in range(self.dep):
            if s + k <= self.size and self.tree[s+k] < v:
                s += k
                v -= self.tree[s+k]
            k //= 2
        return s + 1
  
N, Q = map(int, readline().split())

T = BIT(N+1)
A = [0] + list(map(int, readline().split()))

for i in range(N+1):
    T.add(i+1, A[i])

Ans = []
for _ in range(Q):
    t, a, b = map(int, readline().split())
    if t == 0:
        T.add(a+2, b)
    else:
        Ans.append(T.get(b+1) - T.get(a+1))

print('\n'.join(map(str, Ans)))