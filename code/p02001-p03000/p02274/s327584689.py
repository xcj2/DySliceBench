import sys

infty = 10**10

def merge(A,left,mid,right):

	n1 = mid -left
	n2 = right - mid

	L = [0] * n1
	R = [0] * n2

	for i in range(n1):
		L[i] = A[left+i]
	for i in range(n2):
		R[i] = A[mid+i]

	L.append(infty)
	R.append(infty)

	i = 0
	j = 0
	cnt = 0

	for k in range(left,right):


		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			cnt += len(L) - 1 - i
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

def test():

	n = int(sys.stdin.readline())
	S = list(map(int,sys.stdin.readline().split()))

	result = mergeSort(S,0,n)
	
	print(result)


if __name__ == "__main__":
	test()
