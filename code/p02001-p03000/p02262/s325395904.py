import sys

def print_arr(arr):
	for i in range(len(arr)):
		sys.stdout.write(str(arr[i]))
		if i != len(arr) - 1:
			sys.stdout.write(' ')
	print()

def insertion_sort(arr, g):
	n = len(arr)
	cnt = 0
	for i in range(n):
		key = arr[i]
		j = i - g
		while j >= 0 and arr[j] > key:
			arr[j + g] = arr[j]
			j -= g
			cnt += 1
		arr[j + g] = key
	return cnt

def shell_sort(arr, G):
	cnt = 0
	for i in range(len(G)):
		cnt += insertion_sort(arr, G[i])
	return cnt

def get_gaps(n):
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
arr = [None] * n
for i in range(n):
	arr[i] = int(input())

G = get_gaps(n)
cnt = shell_sort(arr, G)

print(len(G))
print_arr(G)
print(cnt)
for i in range(n):
	print(arr[i])

