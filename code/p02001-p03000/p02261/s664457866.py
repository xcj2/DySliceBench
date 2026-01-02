# Stable Sort

n = int(input())
C = list(input().split(' '))

C1, C2 = [], []
for v in C:
	tmp = v[0]
	num = int(v[1])
	C1.append([tmp, num])
	C2.append([tmp, num])

def bubble(A):
	n = len(A)
	for i in range(n):
		for j in range(n - 1, 0, -1):
			if A[j][1] < A[j - 1][1]:
				A[j], A[j - 1] = A[j - 1], A[j]
	return 0

def selection(A):
	n = len(A)
	for i in range(n):
		minj = i
		for j in range(i, n):
			if A[j][1] < A[minj][1]: minj = j
		A[i], A[minj] = A[minj], A[i]
	return 0

def is_Stable(C1, C2):
	# bubble sort is always stable
	n = len(C1)
	for i in range(n):
		if C1[i][0] != C2[i][0]:
			return False
	return True

def pprint(A):
	res = []
	for v in A:
		tmp1 = v[0]
		tmp2 = str(v[1])
		res.append(tmp1 + tmp2)
	print(*res)
	return
	
bubble(C1)
selection(C2)

pprint(C1)
print('Stable')
pprint(C2)
print('Stable') if is_Stable(C1, C2) else print('Not stable')

