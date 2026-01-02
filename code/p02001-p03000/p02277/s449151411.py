import math
import copy

n = int(input())
A = [None for i in range(n)]
for i in range(n):
    a, b = input().split()
    A[i] = [a, int(b)]
inf = 10**9

def merge(A,left,mid,right):
	#global cnt
	L = A[left:mid] + [[inf,inf]]
	R = A[mid:right] + [[inf,inf]]
	i = 0
	j = 0

	for k in range(left,right):
		#cnt += 1
		if L[i][1] <= R[j][1]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def mergeSort(A,left,right):
	if left + 1 < right:
		mid = (left + right) // 2
		mergeSort(A,left,mid)
		mergeSort(A,mid,right)
		merge(A,left,mid,right)


def partition(A,p,r):
	x = A[r][1]
	i = p
	for j in range(p,r):
		if A[j][1] <= x:
			A[i], A[j] = A[j], A[i]
			i = i+1
	A[i], A[r] = A[r], A[i]

	return i

def quickSort(A,p,r):
	if p < r:
		q = partition(A,p,r)
		quickSort(A,p,q-1)
		quickSort(A,q+1,r)


B = copy.deepcopy(A)
mergeSort(A,0,n)
quickSort(B,0,n-1)

if A == B:
	print("Stable")
else:
	print("Not stable")

ans = [str(x[0]) +" "+str(x[1]) for x in B]
ans = '\n'.join(ans)
print(ans)
