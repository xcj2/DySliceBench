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
	N = II()
	A = LI1()
	L = [0]*N
	b = [0]*N
	t = 1
	for i,a in enumerate(A):
		L[a]+=1
		if(i==0):
			b[0]=t
		else:
			b[i]=b[i-1]+t
		t+=1
	L_s = L.copy()
	L_s.sort(reverse=True)
	max_c = 0
	for l in L_s:
		if l <= 1:
			break
		else:
			max_c += b[l-2]
	ans = [max_c]*N
	for i,a in enumerate(A):
		if(L[a]>=2):
			ans[i]+=(-L[a]+1)
	printV(ans)


if __name__ == '__main__':
	main()