class SegTree:
	"""
	1-indexed
	"""
	def __init__(self,size,funcComp,funcUpd,init_val,undef):
		self.specSize = size
		self.datSize = 1
		self.compareFunc = funcComp		# suppose to min or max
		self.updateFunc = funcUpd		# suppose to add or update
		self.INIT_VAL = init_val	# 0 etc
		self.UNDEFINED_VAL = undef	# 1e18 -1e18 etc
		# num:size以上の最小の2のべき乗
		self.datSize = 2**size.bit_length()

		# the tree is implemented by sequencial list
		self.datTree = [self.INIT_VAL for _ in range(2*self.datSize+1)]

	def update(self, i, val ):
		"""
		i: index(1-indexed)
		bottom-up
		"""
		# i -= 1	# 1-orderで指定され、内部では0-Order想定?
		# i += (self.datSize - 1)
		i += self.datSize
		self.datTree[i] = self.updateFunc(self.datTree[i],val)
		while 0 < i:
			i >>= 1
			self.datTree[i] = self.compareFunc( self.datTree[i<<1|0], self.datTree[i<<1|1] )

	def query(self,a,b):
		""" get minimun/maximum value of range[a,b)
		non-recursive
		bottom-up
		all 1-indexed
		"""
		ret = self.UNDEFINED_VAL

		a += self.datSize
		b += self.datSize
		while a < b:

			if b & 1:
				# shrink right
				b -= 1
				ret = self.compareFunc(ret, self.datTree[b])

			if a & 1:

				# shrink left
				ret = self.compareFunc(ret, self.datTree[a])
				a += 1

			a >>= 1; b >>= 1

		return ret

	def printLeaf(self):
		print(self.datTree[self.datSize-1:])

def update(x,val):
	return val


def LongestSeaquence(A,K):
	N = len(A)
	lis = 0

	# === Range Maximum Query ===
	MAX_A = max(A)
	tree = SegTree(MAX_A,max,update,0,-1e18)
	# tree.update( 0, 1 )

	for n in range(N):
		x = A[n]
		l = max(0,x-K)
		r = min(MAX_A,x+K)
		tmp = tree.query(l,r+1)+1
		tree.update( x, tmp )
		# lis = max(lis, tmp)

	lis=tree.query(0,MAX_A)

	return lis

def main():
	N,K = map(int,input().split())
	A = [ int(input()) for _ in range(N)]

	print(LongestSeaquence(A,K))



if __name__ == "__main__":
	main()