from collections import namedtuple
Card = namedtuple('Card', 'suit value')

def partition(A,p,r):
    x = A[r]
    i = p
    for j in range(p,r):
        if A[j].value <= x.value:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[r] = A[r],A[i]
    return i

def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def isStable(Co,Cs):
    C = Cs[:]
    for ci in Co:
        j = C.index(ci)
        if j > 0:
            if Cs[j-1].value == ci.value:
                return False
        del C[j]
    return True

if __name__=='__main__':
    n = int(input()) 
    Co = list(map(lambda X: Card(X[0],int(X[1])), [input().split() for _ in range(n)]))
    Cs = Co[:]
    quickSort(Cs,0,n-1)
    print("Stable" if isStable(Co,Cs) else "Not stable")
    for c in Cs: print(c.suit,c.value)