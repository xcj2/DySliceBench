import sys
count = 0

def merge_sort(arr):
	merge_sort_(arr, 0, len(arr))

def merge_sort_(arr, left, right):
	if left + 1 < right:
		mid = int(left + (right - left) / 2)
		merge_sort_(arr, left, mid)
		merge_sort_(arr, mid, right)
		merge(arr, left, mid, right)

def merge(arr, left, mid, right):
	global count
	
	n1 = mid - left
	n2 = right - mid
	
#	L = [0] * (n1 + 1)
#	R = [0] * (n2 + 1)
#	for i in range(n1):
#		L[i] = arr[left + i]
#	for i in range(n2):3
#		R[i] = arr[mid + i]
#	L[n1] = R[n2] = sys.maxsize
	
	L = arr[left:left + n1]
	R = arr[mid:mid + n2]
	L.append(sys.maxsize)
	R.append(sys.maxsize)

	i = j = 0
	for k in range(left, right):
		count += 1
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)
print(" ".join(map(str, arr)))
#for i in range(n):
#	print(arr[i], end="")
#	if i != n - 1:
#		print(" ", end="")
#print()
print(count)
