

n, x, y = [0] * 3

def format_input(filename = None):
	global n, x, y
	if filename == None:
		n, x, y = list(map(int, input().split()))

	elif filename == '__random__':
		from random import randint as rng
		n = rng(3, 2 * 10**3)
		x = rng(1, n-1)
		y = rng(x+1, n)
		print(n, x, y)

def distance(i, j):
	return min(abs(j - i), abs(x - i) + abs (y - j) + 1)

def get_answer():
	num_dist = [0] * n
	for i in range(1, n):
		for j in range(i+1, n+1):
			num_dist[distance(i, j)] += 1

	for k in range(1, n):
		print(num_dist[k])

if __name__ == '__main__':
	format_input()

	get_answer()
