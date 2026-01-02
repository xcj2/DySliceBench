import math
import sys


def nontrivial_divisors(x):
	for i in range(1, math.floor(math.sqrt(x)) + 1):
		d, m = divmod(x, i)
		if m == 0:
			if i != x:
				yield i
			if d != x:
				yield d


def solve(n, qs):
	ps = [0] # sent.
	ps.extend(qs)
	balls = [0] * (n + 1)
	vals = [0] * (n + 1)
	divs = [set() for _ in range(n + 1)]
	for i in range(1, n // 2 + 1):
		for j in range(2, n // i + 1):
			divs[i * j].add(i)
	# print(divs, file=sys.stderr)
	first = n // 2 + 1
	last = n
	while True:
		for i in range(first, last + 1):
			if vals[i] % 2 != ps[i]:
				balls[i] += 1
				vals[i] += 1
				for j in divs[i]:
					vals[j] += 1
		if first == 1:
			break
		last = first - 1
		first = last // 2 + 1
	for i in range(1, n + 1):
		if vals[i] % 2 != ps[i]:
			return None
	else:
		bs = [b for b in range(1, n + 1) if balls[b]]
		m = len(bs)
		return m, bs
	

def main():
	n = int(input())
	qs = [int(q) for q in input().split()]
	res = solve(n, qs)
	if res is None:
		print(-1)
	else:
		m, bs = res
		print(m)
		print(*bs)


if __name__ == "__main__":
	main()