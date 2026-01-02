

import re

N = int(input())

def val(stri):
    a = re.sub(r'\D', '', stri)
    a = int(a)
    return a

def bubble_sort(N, A):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if val(A[j]) < val(A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

def selec_sort(N, A):
    for i in range(N):
        minj = i
        for j in range(i + 1, N):
            if val(A[j]) < val(A[minj]):
                minj = j
        A[i], A[minj] = A[minj], A[i]
    return A
    
def isStable(inp, out):
    for i in range(N):
        for j in range(i + 1,N):
            for a in range(N):
                for b in range(a + 1, N):
                    if val(inp[i]) == val(inp[j]) and inp[i] == out[b] and inp[j] == out[a]:
                        return False
    return True



def main():
    A = input().split()

    ST = ''
    for i in A:
        ST += i + ' '
    ST.rstrip(' ')

    bubble_sort(N, A)
    B = ST.split()

    print(*A)
    


    if isStable(A, B):
        print('Stable')
    else:
        print('Not stable')
    A = ST.split()
    selec_sort(N, A)
    B = ST.split()

    print(*A)
    

    if isStable(A, B):
        print('Stable')
    else:
        print('Not stable')

main()


