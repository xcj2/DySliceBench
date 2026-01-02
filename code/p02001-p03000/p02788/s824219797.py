import sys
from bisect import bisect
def input():
	return sys.stdin.buffer.readline()[:-1]

class BIT():#1-indexed
	def __init__(self, size):
		self.table = [0 for _ in range(size+2)]
		self.size = size

	def Get(self, i):#iを返す
		s = 0
		while i > 0:
			s += self.table[i]
			i -= (i & -i)
		return s

	def PointAdd(self, i, x):#
		while i <= self.size:
			self.table[i] += x
			i += (i & -i)
		return

	def SegAdd(self, l, r, x):#lからrにxを足す
		self.PointAdd(l, x)
		self.PointAdd(r+1, -x)
		return


n, d, a = map(int, input().split())
d *= 2
mo = sorted([list(map(int, input().split())) for _ in range(n)])
for i in range(n):
	mo[i][1] = (mo[i][1]-1)//a + 1
reach = []
moo = [x[0] for x in mo]
mooo = [x[1] for x in mo]
for x in moo:
	reach.append(bisect(moo, x+d)-1)
#print(reach)

bit = BIT(n)

ans = 0
for i, h in enumerate(mooo):
	gap = max(0, h - bit.Get(i+1))
	bit.SegAdd(i+1, reach[i]+1, gap)
	ans += gap

print(ans)
