import copy
def BubbleSort(n, A):
    cnt = 0
    flg = True
    while flg:
        flg = False
        for j in range(n-1, 0, -1):
            if int(A[j][1:2]) < int(A[j-1][1:2]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                cnt += 1
                flg = True
    
def SelectionSort(n, B):
    cnt = 0
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if int(B[j][1:2]) < int(B[minj][1:2]):
                minj = j
        if minj != i:
            tmp = B[i]
            B[i] = B[minj]
            B[minj] = tmp
            cnt += 1
    
def IsStable(A, B):
    for a1 in A:
        for b1 in B:
            if int(a1[1:2]) == int(b1[1:2]):
                if a1 == b1:
                    B.remove(b1)
                    break
                else:
                    return "Not stable"
            elif int(a1[1:2]) < int(b1[1:2]):
                break
    return "Stable"
    
n = int(input())
C = input().split()
A = copy.deepcopy(C)
B = copy.deepcopy(C)

BubbleSort(n, A)
print(" ".join(A))
print(IsStable(C, A))

SelectionSort(n, B)
print(" ".join(B))
print(IsStable(C, B))
