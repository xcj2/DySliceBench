

n = 0

def format_input(filename = None):
	global n
	if filename == None:
		n = int(input())

	elif filename == '__random__':
		from random import randint as rng
		n = rng(2, 10**12)
		print(n)

def judge(n, k):
	if n % k == 0:
		return judge(n // k, k)
	else:
		return (n % k == 1)

def get_answer():
	answer = 2
	if n == 2:
		return 1
	for i in range(2, int(n ** 0.5) + 1):
		if (n - 1) % i == 0:
			answer += 2
			if n - 1 == i ** 2:
				answer -= 1
		elif judge(n, i):
			answer += 1
	return answer

if __name__ == '__main__':
	format_input()

	ans = get_answer()
	print(ans)
