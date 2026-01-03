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
	n,a,b = MI()
	S = IS()
	cnt = 0
	frank = 1
	for i,s in enumerate(S):
		if s == 'a':
			if cnt < a+b:
				cnt += 1
				print("Yes")
			else:
				print("No")
		elif s == 'b':
			if cnt < a+b and frank <= b:
				cnt += 1
				frank += 1
				print("Yes")
			else:
				print("No")
		else :
			print("No")

if __name__ == '__main__':
	main()