from sys import stdin, stdout

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def submasks(m):
	s = m
	while s > 0:
		s = (s-1)&m
		yield s

def main():
	n, m, x = rli()
	A = []
	for _ in range(n):
		A.append(list(rli()))
	mask = 0
	for i in range(n):
		mask |= (1 << i)

	opt = INF

	def process(s):
		nonlocal opt
		i = 0
		cost = 0
		algs = [0 for _ in range(m)]
		while s:
			s, bit = divmod(s, 2)
			if bit:
				cost += A[i][0]
				for j in range(1, m+1):
					algs[j-1] += A[i][j]
			i += 1
		if all(skill >= x for skill in algs):
			opt = min(opt, cost)

	process(mask)
	for s in submasks(mask):
		process(s)

	print(opt if opt < INF else -1)
	stdout.close()

if __name__ == "__main__":
	main()