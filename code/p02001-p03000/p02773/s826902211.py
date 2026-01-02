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
	d = {}
	ansl=[]
	max_c = 0
	for _ in range(N):
		s = IS()
		if not s in d:
			d[s]=1
		else:
			d[s]+=1

		if(d[s]>max_c):
				max_c=d[s]
				ansl=[]
				ansl.append(s)
		elif(d[s]==max_c):
			ansl.append(s)
	ansl.sort()
	printV(ansl)


if __name__ == '__main__':
	main()