A = []
ans = 0

def merge(left, mid, right):
	global A
	global ans
	n1 = mid - left
	n2 = right - mid
	l = []
	r = []
	for i in range(n1):
		l += [A[left + i]]
	for i in range(n2):
		r += [A[mid + i]]
	l += [10**18]
	r += [10**18]
	i = 0
	j = 0
	ans += right - left
	for k in range(left, right):
		if l[i] <= r[j]:
			A[k] = l[i]
			i += 1
		else:
			A[k] = r[j]
			j += 1


def Msort(left, right):
	if left + 1 < right:
		mid = int((left + right)/2)
		Msort(left, mid)
		Msort(mid,right)
		merge(left,mid,right)

def main():
	global ans
	global A
	n = int(input())
	A = list(map(int,input().split()))
	Msort(0,n)
	print(" ".join(list(map(str,A))))
	print(ans)

main()
