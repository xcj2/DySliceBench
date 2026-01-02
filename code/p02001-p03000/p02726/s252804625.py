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
	n,x,y = MI()
	x-=1;y-=1
	dist = [0]*(n-1)
	for i in range(n-1):
		for j in range(i+1,n):
			dist[min(abs(j-i), abs(x-i)+1+abs(j-y), abs(y-i)+1+abs(j-x))-1]+=1
	printV(dist)


if __name__ == '__main__':
	main()