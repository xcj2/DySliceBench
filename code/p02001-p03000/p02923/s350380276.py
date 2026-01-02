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
	H = LI()
	H = np.array(H)
	H = H[:-1] >= H[1:]
	ans = 0
	cnt = 0
	for i in range(N-1):
		if H[i]:
			cnt+=1
			ans = max(ans,cnt)
		else:
			cnt=0
	print(ans)

if __name__ == '__main__':
	main()