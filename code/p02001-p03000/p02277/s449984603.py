def partition(A, p, r):
    x = int(A[r-1][1])
    i = p-1

    for j in range(p,r-1):
        if int(A[j][1]) <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r-1] = A[r-1],A[i+1]
    return i + 1

def qsort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        qsort(A,p,q)
        qsort(A,q+1,r)
    return A

def isStable(a):
    length = int(len(a))
    for i in range(length):
        for j in range(i+1,length-1) :
            if a[i][1] == a[j][1] and a[i][2] > a[j][2]:
                return False
                break
    return True

if __name__ == '__main__':
    cnt = int(input())
    A = []
    for i in range(cnt):
        N = input().split()
        N.append(i)
        A.append(N)
    p = 0
    r = len(A)
    B = qsort(A,p,r)
    if isStable(B):
        print("Stable")
    else:
        print("Not stable")
    for i in B:
        print ("{0} {1}".format(i[0],i[1]))