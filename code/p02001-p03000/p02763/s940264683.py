import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

class SegmentTree:
	def __init__(self,N,S):
		self.N = N
		self.tree = [0]*(2*N-1)
		for i,s in enumerate(S):
			self.update(i,s)
	def update(self,i, x):
		i += self.N-1
		self.tree[i] = 1<<int(ord(x)-97)
		while (i > 0):
			i = (i-1) // 2
			self.tree[i] = self.tree[i*2+1] | self.tree[i*2+2]
	def query(self,a,b,k,l,r):
		if(r<=a or b<=l): return 0
		if (a<=l and r<=b) : return self.tree[k]
		else:
			c1 = self.query( a, b, 2 * k + 1, l, (l+r) // 2)
			c2 = self.query( a, b, 2 * k + 2, (l+r) // 2, r)
			return c1 | c2

def count_one_by_shift(num):
	num = (num & 0x55555555) + ((num & 0xAAAAAAAA) >> 1) 
	num = (num & 0x33333333) + ((num & 0xCCCCCCCC) >> 2)
	num = (num & 0x0F0F0F0F) + ((num & 0xF0F0F0F0) >> 4)
	num = (num & 0x00FF00FF) + ((num & 0xFF00FF00) >> 8)
	num = (num & 0x0000FFFF) + ((num & 0xFFFF0000) >> 16)
	return num

def main():
	n = II()
	S = IS()
	N = 1
	while N < n: N*=2
	st = SegmentTree(N,S)
	Q = II()
	ans = []
	for _ in range(Q):
		op, x, y = sys.stdin.readline().split()
		op = int(op)
		if op==1:
			x=int1(x);
			st.update(x,y)
		else:
			x,y=int1(x),int1(y)
			ans.append(count_one_by_shift(st.query(x,y+1,0,0,N)))
	printV(ans)


if __name__ == '__main__':
	main()