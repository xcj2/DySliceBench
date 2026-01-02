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

def count(P):
    res = 0
    T = BIT(N)
    Pi = [None]*N
    for i in range(N):
        Pi[P[i]] = i
    for i in range(N):
        p = Pi[i]
        res += i-T.get(p+1)
        T.add(p+1, 1)
    return res
 

N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
uhalf = -(-N//2)
dhalf = N - uhalf
inf = 10**9+7
ans = inf
for S in range(1<<N):
    card = [A[i] if S&(1<<i) else B[i] for i in range(N)]
    parity = [(1&(S>>i))^(i&1) for i in range(N)]
    even = [(card[i], i) for i in range(N) if parity[i]]
    odd = [(card[i], i) for i in range(N) if not parity[i]]
    if len(even) != uhalf or len(odd) != dhalf:
        continue
    even.sort()
    odd.sort()
    if any(e[0] > o[0] for e, o in zip(even, odd)) or any(e[0] < o[0] for e, o in zip(even[1:], odd)):
        continue
    perm = [even[i//2][1] if not i&1 else odd[i//2][1] for i in range(N)]
    ans = min(ans, count(perm))
print(ans if ans < inf else -1)
