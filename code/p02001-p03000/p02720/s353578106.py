from sys import stdin, stdout
from functools import lru_cache
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()

def num_digs(n):
	return len(str(n))

@lru_cache(None)
def lunlun(n, pos, tight, prev):
	if pos >= len(n):
		return 1
	md = n[pos] if tight else 9
	sd = 1 if pos == 0 else 0
	count = 0
	for d in range(sd, md + 1):
		new_tight = 1 if tight and d == n[pos] else 0
		if (pos == 0) or (d in {prev - 1, prev, prev + 1}):
			count += lunlun(n, pos  + 1, new_tight, d)
	return count 

def lunlun2(n):
	ans = 0
	for i in range(1, num_digs(n)):
		tupn = tuple(9 for _ in range(i))
		pt = lunlun(tupn, 0, 1, 0)
		ans += pt
	tupn = tuple(int(x) for x in str(n))
	ans += lunlun(tupn, 0, 1, 0)
	return ans	

def main():
	k = int(rl())
	n, jump = 10**19, 10**19
	while jump >= 1:
		while n - jump >= 0 and lunlun2(n - jump) >= k:
			n -= jump
		jump //= 2
	stdout.write(str(n));stdout.write("\n")
	stdout.close()

if __name__ == "__main__":
	main()