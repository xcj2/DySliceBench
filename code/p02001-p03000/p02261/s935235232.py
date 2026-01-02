import copy
def BubbleSort(N, A):
    A = copy.deepcopy(A)
    for i in range(N-1):
        for j in range(N-1,i,-1):
            if int(A[j-1][1]) > int(A[j][1]):
                A[j-1], A[j] = A[j], A[j-1]
    return A

def SelectSort(N, A):
    A = copy.deepcopy(A)
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if int(A[j][1]) < int(A[minidx][1]):
                minidx = j
        if minidx != i:
            A[i], A[minidx] = A[minidx], A[i]
    return A

def main():
    n = int(input());  L = input().split()
    B = BubbleSort(n, L)
    S = SelectSort(n, L)
    print(*B); print('Stable')
    print(*S); print('Not stable') if B != S else print('Stable')
main()
