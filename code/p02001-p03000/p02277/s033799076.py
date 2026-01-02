from sys import stdin
N=int(input())
num_list=[]
for i in range(N):
    line = list(stdin.readline().strip().split())
    num_list.append([line[0],int(line[1]),i])
def partition(A,p,r):
    x=A[r][1]
    i=p-1
    for j in range(p,r):
        if A[j][1]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
def check(A):
    for i in range(N-1):
        if A[i][1]==A[i+1][1]:
            if A[i][2]>A[i+1][2]:
                return 0
    return 1
quicksort(num_list,0,N-1)
if check(num_list):
    print("Stable")
else:print("Not stable")
for i in num_list:
    del i[2]
    print(*i)



