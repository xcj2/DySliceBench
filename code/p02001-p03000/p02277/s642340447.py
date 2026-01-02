import copy

INFTY=1000000000
def merge(A,left,mid,right):
    n1=mid-left
    n2=right-mid
    L=[ A[left+i] for i in range(n1)]
    R=[ A[mid+i] for i in range(n2)]
    L.append((INFTY,INFTY))
    R.append((INFTY,INFTY))
    i=0
    j=0
    for k in range(left,right):
        if int(L[i][1])<=int(R[j][1]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
    return right-left

def mergeSort(A,left,right):
    if left+1<right:
        mid=(left+right)//2
        t1=mergeSort(A,left,mid)
        t2=mergeSort(A,mid,right)
        return merge(A,left,mid,right)+t2+t1
    return 0

def partition(A,p,r):
    x=int(A[r][1])
    i=p-1
    for j in range(p,r):
        if int(A[j][1])<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

n=int(input())
A=[input().split() for _ in range(n)]
B=copy.deepcopy(A)

quickSort(A,0,n-1)
mergeSort(B,0,n)
if A==B:
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(' '.join(A[i]))
