def smaller(x, y):
	if x < y:
		return x
	return y

def allzero(lst):
	for i in range(0, len(lst)):
		if lst[i] != 0:
			return False
	return True

def minimum(lst):
	min = 5000000000000000
	for i in range(0, len(lst)):
		min = smaller(min, lst[i])
	return min

N = int(input())
H = list(map(int, input().split()))
sum = 0
while not allzero(H):
	left = -1
	right = -1
	for i in range(0, N):
		if H[i] != 0:
			left = i
			break
	for i in range(left, N):
		if H[i] == 0:
			right = i
			break
	if right == -1:
		right = N
	min = minimum(H[left:right])
	sum += min
	for i in range(left, right):
		H[i] -= min
print(sum)