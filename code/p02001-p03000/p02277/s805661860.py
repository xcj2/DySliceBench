import copy

def partition(A, p, r):
    x = int(A[r][1])
    i = p-1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def show(l):
    for i in range(len(l)):
        print(l[i][0], l[i][1], sep = ' ')
    

n = int(input())
l_1 = []
for _ in range(n):
    a = input().split()
    l_1.append(a)
l_2 = copy.deepcopy(l_1)

quickSort(l_1, 0, n-1)

for i in range(n-1):
    if int(l_1[i][1]) == int(l_1[i+1][1]):
        if l_2.index(l_1[i]) > l_2.index(l_1[i+1]):
            print('Not stable')
            break
else:  
    print('Stable')

show(l_1)
