import copy

def Bubble(A,N):
	flag = 1
	while flag:
		flag = 0
		for i in range(N-1,0,-1):
			if int(A[i][1]) < int(A[i-1][1]):
				tmp = A[i]
				A[i] = A[i-1]
				A[i-1] = tmp
				flag = 1

def Selection(A,N):
	for i in range(N):
		minj = i
		for j in range(i,N):
			if int(A[j][1]) < int(A[minj][1]):
				minj = j
		tmp = A[i]
		A[i] = A[minj]
		A[minj] = tmp

def isStable(A,B,N):
	for i in range(N):
		if A[i] != B[i]:
			return False
	return True

N = int(input())
A = list(input().split())
B = copy.deepcopy(A)
Bubble(A,N)
Selection(B,N)
print(' '.join([str(a) for a in A]))
print('Stable')
print(' '.join([str(a) for a in B]))
print('Stable') if isStable(A,B,N) else print('Not stable')

