import copy

n = int(input())
A = []

for i in range(n):
    x, y = input().split()
    z = {'mark': x, 'num': int(y)}
    A.append(z)

B = copy.deepcopy(A)

def partition(p, r):
    i = p
    for j in range(p, r):
        if A[j]['num'] <= A[r]['num']:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quicksort(p, r):
    if p < r:
        q = partition(p, r)
        quicksort(p, q-1)
        quicksort(q+1, r)

quicksort(0, n-1)

def checkstable():
    for i in range(n-1):
        if A[i]['num'] == A[i+1]['num']:
            if B.index(A[i]) > B.index(A[i+1]):
                return 'Not stable'
                break
    return 'Stable'

print(checkstable())
for i in A:
    print(i['mark'], i['num'])
