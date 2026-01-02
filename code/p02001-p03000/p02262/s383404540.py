import sys

def print_arr(arr):
	for i in range(len(arr)):
		sys.stdout.write(str(arr[i]))
		if i != len(arr) - 1:
			sys.stdout.write(' ')
	print()

def insertion_sort(arr, n, g):
	cnt = 0
	for i in range(g, n):
		v = arr[i]
		j = i - g
		while j >= 0 and arr[j] > v:
			arr[j + g] = arr[j]
			j = j - g
			cnt += 1
		arr[j + g] = v
	return cnt

def shell_sort(arr, g):
	cnt = 0
	for i in range(len(g)):
		cnt += insertion_sort(arr, len(arr), g[i])
	return cnt

def get_gap(n):
	lst = []
	v = 1
	cnt = 1
	while v <= n:
		lst.append(v)
		v += 3**cnt
		cnt += 1
	if len(lst) == 0: lst.append(1)
	return list(reversed(lst))

n = int(input())
arr = [0] * n
for i in range(n):
	arr[i] = int(input())

g = get_gap(n)
m = len(g)
cnt = shell_sort(arr, g)

print(m)
print_arr(g)
print(cnt)
for i in range(n):
	print(arr[i])

