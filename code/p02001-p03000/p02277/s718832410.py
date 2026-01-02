def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i = i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def merge(A, left, mid, right):
    L=A[left:mid]+[["X",10000000000]]
    R=A[mid:right]+[["X",10000000000]]
    i = 0
    j = 0

    for k in range(left,right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, left, right):
    mid=0
    if left+1 < right:
        mid = int((left + right)/2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
import copy
n=int(input())
A=[]
for i in range(n):
    Astr=input().split( )
    A.append([Astr[0],int(Astr[1])])

B=A.copy()
#print(id(A))      # ID: 4315448960
#print(id(B))      # ID: 4315448960

quickSort(A,0,n-1)

mergeSort(B,0,n)
#print(*B)
flag=0
for i in range(n):
    if A[i]!=B[i]:
        flag=1
        break
    else:
        pass
if flag==1:
    print("Not stable")
else:
    print("Stable")

#print(*A)
#print(*B)
for i in range(n):
    print(*A[i])

