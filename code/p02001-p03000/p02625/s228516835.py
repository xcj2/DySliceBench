import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

class CombMod:
	def __init__(self, N):
		facts = [1]
		rfacts = [1]
		for i in range(1, N+1):
			facts.append(facts[i-1]*i % mod)
			rfacts.append(pow(facts[i], mod-2, mod))
		self.facts = facts
		self.rfacts = rfacts

	def comb(self, n, k):
		return self.facts[n]*self.rfacts[k]*self.rfacts[n-k] % mod

	def perm(self, n, k):
		return self.facts[n]*self.rfacts[n-k] % mod

	def fact(self, k):
		return self.facts[n] % mod

	def rfact(self, k):
		return self.rfacts[n] % mod

N, M = rl()
cm = CombMod(M)

ans = 0
for i in range(0, N+1):
	ans += (-1)**i * cm.perm(M, i) * (cm.perm(M-i, N-i)**2) * cm.comb(N, i)
	ans = ans % mod
print(ans)
