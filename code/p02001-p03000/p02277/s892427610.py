import sys
def input():
    return sys.stdin.readline()[:-1]
    
n = int(input())
A = []

for i in range(n):
    a,num = input().split()
    A.append([a,int(num),i])
    
def partition(A,p,r):
    #import random
    #rand = 1+int(p+(r-p)*random.random())
    #A[rand],A[r] = A[r],A[rand]    
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1]<= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
        
quickSort(A,0,n-1)

def check_stable(A):
    for i in range(n-1):
        if (A[i][1] == A[i+1][1]) & (A[i][2]>A[i+1][2]):
            return "Not stable"
    return "Stable"

print(check_stable(A))

for a,num,_ in A:
    print(*[a, num])
