def partition(A, l, r):
    """ partition A[l:r] using q(A[r]) and return q's index
    """
    q = A[r][1]
    sep_i = l # left elements of seq <= q < right ones
    for j in range(l, r):
        if A[j][1] <= q:
            # A[j] is left element
            
            # add A[j] to last of left, and replace first of right to last
            A[sep_i], A[j] = A[j],  A[sep_i]
            sep_i += 1 # update separator
        else:
            # A[j] is right element
            pass

    A[sep_i], A[r] = A[r], A[sep_i]
    
    return sep_i

def quick_sort(A, l, r):
    if l < r:
        q = partition(A, l, r-1)
        quick_sort(A, l, q)
        quick_sort(A, q+1, r)

def is_stable(A, B):
    cA = list(A)
    for x in B:
        i = cA.index(x)
        if i == 0:
            pass
        elif cA[i - 1][1] == x[1]:
            return False
        del cA[i]
    return True

A = []
r = int(input())
for _ in range(r):
    mark, num = input().split()
    A.append([mark, int(num)])

B = list(A)
quick_sort(A, 0, r)

if is_stable(A, B):
    print('Stable')
else:
    print('Not stable')

for x in A:
    print(*x)
