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
	N,M = MI()
	NUM = [-1]*N
	ch = True
	for i in range(M):
		s,c = MI()
		s = s-1
		if(NUM[s]!=-1 and NUM[s]!=c):
			ch = False
		NUM[s]=c
	if(NUM[0]==0 and N!=1):
		ch=False
	if(ch==False):
		print(-1)
	else:
		ans = 0
		t = 10**(N-1)
		for i in range(N):
			if(NUM[i]==-1 and i==0):
				if(N!=1):
					ans += t
			elif(NUM[i]!=-1):
				ans += (t * NUM[i])
			t //= 10

		print(ans)




if __name__ == '__main__':
	main()