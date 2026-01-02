from sys import stdin, stdout
from collections import defaultdict

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()

def main():
	n, m, q = (int(x) for x in rll())
	pts = defaultdict(lambda: 0)
	for _ in range(q):
		a, b, c, d = (int(x) for x in rll())
		pts[(a, b, c)] = d

	seq = []
	ans = float('-inf')

	def calcval(s):
		score = 0
		curr = defaultdict(lambda: 0)
		for (a, b, c), d in pts.items():
			if s[b-1] - s[a-1] == c and d > curr[(a, b)]:
				score -= curr[(a,b)]
				curr[(a,b)] = d
				score += d
		return score

	def dfs(i, maxlen, maxdig, prev = None):
		nonlocal ans
		if i == maxlen:
			score = calcval(seq)
			ans = max(ans, score)
			return
		start = 1 if prev is None else prev
		for num in range(start, maxdig + 1):
			seq.append(num)
			dfs(i+1, maxlen, maxdig, num)
			seq.pop()

	dfs(0, n, m)
	stdout.write(str(ans));stdout.write("\n")
	stdout.close()

if __name__ == "__main__":
	main()