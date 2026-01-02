def bubble_sort(A, n):
	flag = 1
	i = 0

	while flag:
		flag = 0
		for j in range(n-1, i, -1):
			if int(A[j][1]) < int(A[j-1][1]):
				A[j], A[j-1] = A[j-1], A[j]
				flag = 1

		i += 1
	
	return A

def selection_sort(A, n):
	for i in range(n-1):
		minj = i
		for j in range(i, n):
			if int(A[j][1]) < int(A[minj][1]):
				minj = j

		if i != minj:
			A[i], A[minj] = A[minj], A[i]

	return A

def is_stable(A, B, n):
	for i in range(0, n):
		for j in range(i+1, n):
			for a in range(0, n):
				for b in range(a+1, n):
					if int(A[i][1]) == int(A[j][1]) and A[i] == B[b] and A[j] == B[a]:
						return False

	return True

def print_stable(flag):
	if flag:
		print('Stable')
	else:
		print('Not stable')

if __name__ == '__main__':
	n = int(input())
	A = list(input().split())
	A2 = A[:]

	B = bubble_sort(A, n)
	print(' '.join(B))
	print_stable(is_stable(A, B, n))

	B = selection_sort(A2, n)
	print(' '.join(B))
	print_stable(is_stable(A, B, n))