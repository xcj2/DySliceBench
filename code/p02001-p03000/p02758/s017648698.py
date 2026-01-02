import sys
from bisect import bisect
def input():
	return sys.stdin.buffer.readline()[:-1]

MOD = 998244353
n = int(input())
r = []
for _ in range(n):
	x, d = map(int, input().split())
	r.append((-x, -x-d))
r.sort()

INF = 10**30

class Rmin():
	def __init__(self, size):
		#the number of nodes is 2n-1
		self.n = 1
		while self.n < size:
			self.n *= 2
		self.node = [INF] * (2*self.n-1)

	def Access(self, x):
		return self.node[x+self.n-1]

	def Update(self, x, val):
		x += self.n-1
		self.node[x] = val
		while x > 0:
			x = (x-1)//2
			self.node[x] = min(self.node[2*x+1], self.node[2*x+2])
		return

	#[l, r)
	def Get(self, l, r):
		L, R = l+self.n, r+self.n
		s = INF
		while L<R:
			if R & 1:
				R -= 1
				s = min(s, self.node[R-1])
			if L & 1:
				s = min(s, self.node[L-1])
				L += 1
			L >>= 1
			R >>= 1
		return s

leftmost = Rmin(n)

wait = [r[0][0]]
dp = [[0 for _ in range(2)] for _ in range(n)]#0: いない 1: いる
dp[0] = [1, 1]
leftmost.Update(0, 0)

for i in range(1, n):
	dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD	
	if r[i][1] < wait[-1]:
		b = bisect(wait, r[i][1])
		mi = leftmost.Get(b, i)
		dp[i][0] = dp[mi][0]
		leftmost.Update(i, mi)
	else:
		dp[i][0] = dp[i][1]
		leftmost.Update(i, i)
	wait.append(r[i][0])

print((dp[n-1][0] + dp[n-1][1]) % MOD)