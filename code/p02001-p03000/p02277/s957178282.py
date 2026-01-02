n=int(input())
a=[]
for i in range(n):
	x,y=input().split()
	a.append([int(y),x])
from copy import copy
b=copy(a)

def partition(A,p,r):
	x=A[r][0]
	i=p-1
	for j in range(p,r):
		if A[j][0]<=x:
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[r]=A[r],A[i+1]
	return i+1

def Quick(A,p,r):
	if p<r:
		q=partition(A,p,r)
		Quick(A,p,q-1)
		Quick(A,q+1,r)

def Merge(A, left, mid, right):
	n1 = mid - left
	n2 = right - mid
	L=[[0,"ST"]for _ in range(n1+1)]
	R=[[0,"ST"]for _ in range(n2+1)]
	for i in range(n1):
		L[i] = A[left + i]
	for i in range(n2):
		R[i] = A[mid + i]
	L[n1][0] = 10**10
	R[n2][0] = 10**10
	i = 0
	j = 0
	for k in range(left,right):
		if L[i][0] <= R[j][0]:
			A[k] = L[i]
			i+=1
		else:
			A[k] = R[j]
			j+=1

def MergeSort(A, left, right):
	if left+1 < right:
		mid = (left + right)//2
		MergeSort(A, left, mid)
		MergeSort(A, mid, right)
		Merge(A, left, mid, right)
MergeSort(a,0,n)
Quick(b,0,n-1)
print("Stable" if a==b else "Not stable")
for i in range(n):
	print(b[i][1],b[i][0])


