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
	n,k = MI()
	mod = 10**9+7

	def f(n,r,mod):
		if (r < 0) or (n < r):
			return 0
		r = min(r, n-r)
		return fact[n] * factinv[r] * factinv[n-r] % mod

	fact = [1,1]
	factinv = [1,1]
	inv = [0,1]

	for i in range(2,n+1):
		fact.append((fact[-1]*i)%mod)
		inv.append((-inv[mod % i] * (mod // i)) % mod)
		factinv.append((factinv[-1] * inv[-1]) % mod)

	ans = 1
	for m in range(1,min(n,k)+1):
		ans += (f(n,m,mod) * f(n-1, m, mod)) % mod
		ans %= mod

	print(ans)

if __name__ == '__main__':
	main()