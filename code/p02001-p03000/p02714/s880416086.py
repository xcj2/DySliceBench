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

def main():
	n = II()
	s = IS()
	r,g,b=[],[],[]

	def binary_search(lst, K):
		l = 0; r = len(lst);
		while(l+1<r):
			mid = (l+r)//2
	    #下記の操作を書き換えることによって探索条件を変更可能
			if(lst[mid]>K): r=mid
			else: l=mid
		return l

	for i,ss in enumerate(s):
		if ss=='R':
			r.append(i)
		elif ss=='G':
			g.append(i)
		else:
			b.append(i)
	ans=len(r)*len(g)*len(b)
	for rr in r:
		for gg in g:
			a=max(rr,gg)+abs(rr-gg)
			if(a<n):
				if(s[a]=="B"):
					ans-=1
			a=min(rr,gg)-abs(rr-gg)
			if(a<n and a>=0):
				if(s[a]=="B"):
					ans-=1
			if((rr+gg)%2==0):
				a=(rr+gg)//2
				if(a<n):
					if(s[a]=="B"):
						ans-=1
	print(ans)







if __name__ == '__main__':
	main()