import sys
from collections import defaultdict

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
mo = 10**9+7

def main():
	s =II()
	dic = defaultdict(lambda : False)
	idx = 1
	while(True):
		if idx!=1:
			if s%2==0:
				s/=2
			else:
				s=3*s+1
		if dic[s]:
			print(idx)
			exit()
		else:
			dic[s]=True
		idx+=1


if __name__ == '__main__':
	main()