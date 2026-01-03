def main():
	n = int(input())
	s = int(input())
	ans = solve(n, s)
	print(ans)

def solve(n: int, s: int) -> int:
	if n == s:
		return n+1

	def f(b:int, n:int) -> int:
		if b < 2:
			return -1
		if b > n:
			return n
		cur = n
		ans = 0
		while cur > 0:
			ans += cur%b
			cur //= b
		return ans

	sqrtn = int(n**0.5)
	for i in range(2, sqrtn):
		this_ans = f(i, n)
		if this_ans == s:
			return i

	for p in range(sqrtn+1, 0, -1):
		if (n-s)%p != 0:
			continue
		b = (n-s)//p + 1
		if f(b, n) == s:
			return b
	return -1


if __name__ == '__main__':
	main()