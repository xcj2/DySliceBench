comparison = 0

def merge(A,left,mid,right):
    global comparison
    n1 = mid - left
    n2 = right - mid
    L = [0]*(n1+1)
    R = [0]*(n2+1)

    for i in range(n1):
        L[i] = A[left+i]
    for i in range(n2):
        R[i] = A[mid+i]
    
    L[n1] = 1e12
    R[n2] = 1e12

    i = 0
    j = 0

    for k in range(left,right):
        comparison += 1
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergesort(A,left,right):
    if left+1 < right:
        mid = (left+right)//2
        mergesort(A,left,mid)
        mergesort(A,mid,right)
        merge(A,left,mid,right)

def main():
    n = int(input())
    A = list(map(int,input().split()))
    mergesort(A,0,n)
    print(*A)
    print(comparison)

if __name__ == "__main__":
    main()
