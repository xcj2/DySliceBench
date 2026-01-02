def _level(n):
	if n == 0:
		return 1
	else:
		return 3 + 2 * level(n-1)

def _eat(n, x):
	if n == 0:
		return 1 if x > 0 else 0
	if x <= 1:
		return 0
	if x <= 1 + level(n-1):
		return eat(n-1, x-1)
	if x == 1 + level(n-1) + 1:
		return eat(n-1, level(n-1)) + 1
	if x <= 1 + level(n-1) + 1 + level(n-1):
		return eat(n-1, level(n-1)) + 1 + eat(n-1, x - (1 + level(n-1) + 1))
	else:
		return eat(n-1, level(n-1)) + 1 + eat(n-1, level(n-1))

store = {}

def level(n):
	if n not in store:
		store[n] = _level(n)
	return store[n]

def eat(n, x):
	if (n, x) not in store:
		store[(n, x)] = _eat(n, x)
	return store[(n, x)]


print(eat(*map(int, input().split())))
