class Num:
    a=0
    b=0
    origin=0

def partition(A, p, r):
    x=A[r].b
    i=p-1
    for j in range(p,r):
        if A[j].b <= x:
            i += 1
            A[i].b,A[j].b = A[j].b,A[i].b
            A[i].a,A[j].a = A[j].a,A[i].a
            A[i].origin,A[j].origin = A[j].origin,A[i].origin
    A[i+1].b,A[r].b = A[r].b,A[i+1].b
    A[i+1].a,A[r].a = A[r].a,A[i+1].a
    A[i+1].origin,A[r].origin = A[r].origin,A[i+1].origin
    return i+1
def quick_sort(A , p, r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
def isStable(A):
    flag=True
    n=len(A)
    for i in range(n-1):
        if A[i].b == A[i+1].b and A[i].origin > A[i+1].origin:
            flag = False
    return flag

if __name__ == "__main__":
    
    n=int(input())
    A=[]
    for i in range(n):
        num =Num()
        a=input().split()
        num.a = a[0]
        num.b = int(a[1])
        num.origin=i
        A.append(num)
    quick_sort(A,0,n-1)
    if isStable(A):
        print("Stable")
    else:
        print("Not stable")
    for i in A:
        print(i.a,end=" ")
        print(i.b)
            
    
