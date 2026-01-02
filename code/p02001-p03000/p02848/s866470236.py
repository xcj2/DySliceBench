import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N = II()
	S = sys.stdin.readline()
	ans = ''
	for i in range(len(S)-1):
		if ord(S[i])+N > 90:
			ans += chr((ord(S[i])+N)%91 + 65)
		else:
			ans += chr((ord(S[i])+N))
	print(ans)

main()