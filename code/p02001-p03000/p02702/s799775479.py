import collections
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def naive(s):
	cnt = 0
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			k = int(s[i:j])
			if k % 2019 == 0 and k != 0:
				#print(i, j)
				cnt += 1
	return cnt

def main(s):
	nums = [0]
	cur = 0
	p = 0.1
	for i in range(len(s)):
		p = int(p * 10) % 2019
		cur = (cur + int(s[len(s) - 1 - i]) * p) % 2019
		nums.append(cur)
	d = dict(collections.Counter(nums))
	a = [val for key, val in d.items() if val >= 2]
	return sum([comb(x, 2) for x in a])	

s = input()
print(main(s))