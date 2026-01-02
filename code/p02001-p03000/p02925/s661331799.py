import sys
input = sys.stdin.buffer.readline

def f(g: list, deg: list):
	l = len(g)
	depth = [0] * l
	ret = []
	q = []
	for i, d in enumerate(deg):
		if not d:
			ret.append(i)
			q.append(i)
	while q:
		cur = q.pop(0)
		for nxt in g[cur]:
			deg[nxt] -= 1
			if not deg[nxt]:
				depth[nxt] = depth[cur] + 1
				ret.append(nxt)
				q.append(nxt)
	if l > len(ret):
		return False
	return max(depth)

def label(a, b, n):
	if a > b:
		a, b = b, a
	return (a - 1) * (2 * n - a) // 2 + b - a - 1


def main():
	n = int(input())
	g = [[] for _ in range(n * (n - 1) // 2)]
	deg = [0] * (n * (n - 1) // 2)
	for i in range(1, n + 1):
		l = list(map(int, input().split()))
		for x, y in zip(l, l[1:]):
			t = label(i, y, n)
			g[label(i, x, n)].append(t)
			deg[t] += 1
	depth = f(g, deg)
	if not depth:
		print(-1)
		exit()
	print(depth + 1)

if __name__ == "__main__":
	main()
