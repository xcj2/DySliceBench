import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

K = ri()
S = rs()

class CombMod:
    def __init__(self, N):
        self.fact = [1]
        self.rfact = [1]
        for i in range(1, N+1):
            self.fact.append(self.fact[i-1]*i % mod)
            self.rfact.append(pow(self.fact[i], mod-2, mod))

    def comb(self, n, k):
        return self.fact[n]*self.rfact[k]*self.rfact[n-k] % mod

class PowMod:
	def __init__(self, N, base=[2]):
		self.mem = {}
		for b in base:
			pows = [1]
			for i in range(1, N+1):
				pows.append(pows[-1]*b % mod)
			self.mem[b] = pows

	def pow(self, b, n):
		return self.mem[b][n]

N = len(S)
cm = CombMod(K+N)
pm = PowMod(K, base=[25, 26])

ans = 0
for i in range(K+1):
	ans += cm.comb(K+N-i-1, N-1) * pm.pow(26, i) * pm.pow(25, K-i)
	ans = ans % mod
print(ans)
