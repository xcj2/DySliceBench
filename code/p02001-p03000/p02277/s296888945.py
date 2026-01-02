def partition(A,p,r):
    x = A[r][1]
    i=p-1
    for j in range(p,r):
        if A[j][1]<=x:
            i=i+1
            (A[i],A[j])=(A[j],A[i])
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1

def quickSort(A, p, r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def checker(A,start,end):
    for i in range(start,end-1):
        if A[i][1]==A[i+1][1]:
            if A[i][2]>A[i+1][2]:
                return "Not stable"
    return "Stable"

n = int(input())
l = []
for i in range(n):
    card = input().split()
    l.append((card[0],int(card[1]),i))
quickSort(l,0,n-1)
print(checker(l,0,n))
for s,n,c in l:
    print("{} {}".format(s,n))