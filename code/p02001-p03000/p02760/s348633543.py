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
	a = []
	for _ in range(3):
		a.append(LI())
	a = np.array(a)
	n = II()
	b = np.array([[False for _ in range(3)] for _ in range(3)])
	for _ in range(n):
		b = np.logical_or(b,a==II())
	if (b[0][0] and b[0][1] and b[0][2]) or (b[1][0] and b[1][1] and b[1][2]) or (b[2][0] and b[2][1] and b[2][2]) or (b[0][0] and b[1][0] and b[2][0]) or (b[0][1] and b[1][1] and b[2][1]) or (b[0][2] and b[1][2] and b[2][2]) or (b[0][0] and b[1][1] and b[2][2]) or (b[0][2] and b[1][1] and b[2][0]) :
		print("Yes")
	else:
		print("No")



if __name__ == '__main__':
	main()