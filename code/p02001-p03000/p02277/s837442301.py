import copy

INF = 10 ** 10
def merge(A, left, mid, right):
	count = 0
	L = A[left:mid] + [(INF, INF)]
	R = A[mid:right] + [(INF, INF)]

	i, j = 0, 0
	for k in range(left, right):
		count += 1
		if L[i][1] <= R[j][1]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
	return count

def mergeSort(A, left, right):
	if left + 1 < right:
		mid = (left + right) // 2
		countL = mergeSort(A, left, mid)
		countR = mergeSort(A, mid, right)
		return merge(A, left, mid, right) + countL + countR
	return 0

def partition(A, p, r):
	x = A[r][1]
	i = p - 1
	for j in range(p, r):
		if A[j][1] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1

def quickSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quickSort(A, p, q - 1)
		quickSort(A, q + 1, r)

n = int(input())
A = [None for _ in range(n)]
for i in range(n):
	a, b = input().split()
	A[i] = (a, int(b))

B = copy.deepcopy(A)
quickSort(A, 0, n - 1)
mergeSort(B, 0, n)

if A == B:
	print("Stable")
else:
	print("Not stable")

for i in range(n):
	print(" ".join(map(str, A[i])))
