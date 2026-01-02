INF = 10**30

class Rmax():
	def __init__(self, size):
		#the number of nodes is 2n-1
		self.n = 1
		while self.n < size:
			self.n *= 2
		self.node = [-INF] * (2*self.n-1)

	def Access(self, x):
		return self.node[x+self.n-1]

	def Update(self, x, val):
		x += self.n-1
		self.node[x] = val
		while x > 0:
			x = (x-1)//2
			self.node[x] = max(self.node[2*x+1], self.node[2*x+2])
		return

	#[l, r)
	def Get(self, l, r):
		L, R = l+self.n, r+self.n
		s = -INF
		while L<R:
			if R & 1:
				R -= 1
				s = max(s, self.node[R-1])
			if L & 1:
				s = max(s, self.node[L-1])
				L += 1
			L >>= 1
			R >>= 1
		return s

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

n, k = map(int, input().split())
p = list(map(int, input().split()))
ma, mi = Rmax(n), Rmin(n)
for i in range(n):
	ma.Update(i, p[i])
	mi.Update(i, p[i])
ans = n-k+1
same = set()
tmp = 0
for i in range(1, n):
	if p[i-1] < p[i]:
		tmp += 1
	else:
		tmp = 0
	if tmp >= k-1:
		same.add(i-k+1)
ans -= max(0, len(same)-1)
for i in range(k, n):
	if p[i-k] < mi.Get(i-k+1, i) and ma.Get(i-k+1, i) < p[i]:
		if not i-k in same and not i-k+1 in same:
			ans -= 1
print(ans)