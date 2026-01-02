import sys
import copy

infty = 10**10

def merge(A,left,mid,right):

	n1 = mid -left
	n2 = right - mid

	L = []
	R = []

	for i in range(n1):
		L.append(A[left+i])
	for i in range(n2):
		R.append(A[mid+i])

	eInfty = ['X',infty]
	L.append(eInfty)
	R.append(eInfty)

	i = 0
	j = 0
	cnt = 0

	for k in range(left,right):

		cnt += 1

		if L[i][1] <= R[j][1]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
		

	return cnt


def mergeSort(A,left,right):

	cnt = 0

	if left+1 < right:

		mid = (left + right) // 2
		cnt += mergeSort(A,left,mid)
		cnt += mergeSort(A,mid,right)
		cnt += merge(A,left,mid,right)

	return cnt


def Partition(A,p,r):

	# choose pivot
	#A[r],A[r//2] = A[r//2],A[r]

	x = A[r][1]
	i = p-1
	for j in range(p,r):

		if A[j][1] <= x:

			i += 1
			A[i],A[j] = A[j],A[i]

	A[i+1],A[r] = A[r],A[i+1]

	return i+1

def Quicksort(A,p,r):

	if p < r:

		q = Partition(A,p,r)
		Quicksort(A,p,q-1)
		Quicksort(A,q+1,r)

def isStable(M,Q):

	for i in range(len(M)):

		if M[i] != Q[i]:

			return False

	return True

def test():

	n = int(sys.stdin.readline())
	deck = []

	for i in range(n):

		inputs = list(sys.stdin.readline().split())
		inputs[1] = int(inputs[1])

		deck.append(inputs)

	original = copy.deepcopy(deck)
	result = mergeSort(original,0,n)

	Quicksort(deck,0,n-1)

	if isStable(original,deck) == True:
		print("Stable")
	else:
		print("Not stable")

	for i in range(n):
		print(f"{deck[i][0]} {deck[i][1]}")


if __name__ == "__main__":
	test()

