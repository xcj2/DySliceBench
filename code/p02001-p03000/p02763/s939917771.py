import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

class BIT:
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n+1)
        
    def add(self, i, x):
        n, nums = self.n, self.nums
        i += 1
        while i <= n:
            nums[i] += x
            i += i & -i
    
    def sum(self, i):
        nums = self.nums
        s = 0
        i += 1
        while i:
            s += nums[i]
            i -= i & -i
        return s
    
    def search(self, x):
        n, nums = self.n, self.nums
        s, p = 0, 0
        for i in range(n.bit_length(), -1, -1):
            np = p + (1<<i)
            if np <= n and s+nums[np] < x:
                s += nums[np]
                p = np
        return p


N = ri()
S = rs()
Q = ri()
queries = []
for i in range(Q):
	q = rs().split()
	if q[0] == '1':
		q = (int(q[0]), int(q[1])-1, q[2])
	else:
		q = (int(q[0]), int(q[1])-1, int(q[2])-1)
	queries.append(q)

import collections
h = collections.defaultdict(lambda: BIT(N))

S = list(S)
for i, s in enumerate(S):
	h[s].add(i, 1)
for q in queries:
	if q[0] == 1:
		i, c = q[1], q[2]
		h[S[i]].add(i, -1)
		h[c].add(i, 1)
		S[i] = c
	else:
		l, r = q[1], q[2]
		cnt = 0
		for c, bit in h.items():
			if bit.sum(r) - bit.sum(l-1) > 0:
				cnt += 1
		print(cnt)
