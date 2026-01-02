import sys
import numpy as np

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
	X = LI()
	X.sort()
	X = np.array(X)
	X2 = X ** 2
	m0 = np.sum(X) // N
	m1 = m0+1
	print(min(np.sum(X2) - 2*m0*np.sum(X) + N*m0**2, np.sum(X2) - 2*m1*np.sum(X) + N*m1**2))

if __name__ == '__main__':
	main()