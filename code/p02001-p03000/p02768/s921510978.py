import sys,math

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
	mod = 10 ** 9 + 7

	def f(n,r,mod):
		r = min(r,n-r)
		x = y = 1
		for i in range(r):
			x = (x*(n-i)) % mod
			y = (y*(i+1)) % mod
		return (x * pow(y, mod-2, mod)) % mod

	ans = pow(2,n,mod) - f(n,a,mod) - f(n,b,mod) - 1
	ans += mod if ans < 0 else 0
	ans += mod if ans < 0 else 0
	print(ans)

if __name__ == '__main__':
	main()