
def showList(A, N):
    for i in range(N-1):
        print(A[i],end=' ')
    print(A[N-1])

def get_intlist(A):
    list_int = [int(x[1:]) for x in A]
    return list_int 

def bubbleSort(A, N):
    """
    バブルソート
    O(n^2)のアルゴリズム
    """
    B = get_intlist(A)
    flag = 1
    count = 0
    while flag:
        flag = 0
        for i in range(N-1, 0, -1):
            if B[i] < B[i-1]:
                v = A[i]
                A[i] = A[i-1]
                A[i-1] = v

                v = B[i]
                B[i] = B[i-1]
                B[i-1] = v
                flag = 1
    return A

def selectionSort(A, N):
    """
    選択ソート
    O(n^2)のアルゴリズム
    """
    B = get_intlist(A)
    for i in range(N):
        minj = i
        for j in range(i,N):
            if B[j] < B[minj]:
                minj = j
        if minj != i:
            t = B[minj]
            B[minj] = B[i]
            B[i] = t

            t = A[minj]
            A[minj] = A[i]
            A[i] = t
    return A

N = int(input())
A = [x for x in input().split(' ')]
A_ss = A.copy()
bub = bubbleSort(A,N)
showList(bub,N)
print('Stable')
sel = selectionSort(A_ss,N)
showList(sel,N)
if sel == bub:
    print('Stable')
else:
    print('Not stable')
