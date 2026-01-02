"""Quick Sort."""
 
def partition(A, p, r):
    """Divide list A into A[p:q] whose elements aren't greater than A[q] and
    A[q+1:r] whose elements are greater than A[q].
 
    Each element of A is a list [x, y].
    x is a character of S, H, C or D (trump suits).
    y is a natural number.
    Sorting is done based on y numbers.
     
    Default value of p is 0.
    The number as a refernce of the division is A[r].
     
    Return the index q.
    """
 
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
 
 
def quickSort(A, p, r):
    """Sort list A in ascending order with quick sort algorithm.
 
    Default value of p is 0 (the start index).
    r is 1 less than the length of A (the last index of A).
    """
 
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
 
 
def is_stable(A, B):
    """Check the stability of sorted list A.
 
    A is a sorted list.
    B is a original list.
 
    Return True or False.
    """
 
    cA = list(A)
    for x in B:
        i = cA.index(x)
        if i == 0:
            pass
        elif cA[i - 1][1] == x[1]:
            return False
        del cA[i]
    return True
 
 
 
import sys
 
r = int(sys.stdin.readline()) - 1
 
A = []
 
for x in sys.stdin.readlines():
    suit, num = x.split()
    num = int(num)
    A.append([suit, num])
 
B = list (A)
 
quickSort(A, 0, r)
 
if is_stable(A, B):
    print('Stable')
else:
    print('Not stable')
 
for x in A:
    print(*x)