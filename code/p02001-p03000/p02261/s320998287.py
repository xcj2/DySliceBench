import copy

def bubble_sort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]

def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def is_stable(in0, out0):
    for m in '123456789':
        in1 = list(filter(lambda e:e[1]==m, in0))
        out1 = list(filter(lambda e:e[1]==m, out0))
        #print(in1,out1)
        if in1 != out1:
            return 'Not stable'
    return 'Stable'

N = int(input())
C = list(input().split())
C1 = copy.deepcopy(C)
C2 = copy.deepcopy(C)
bubble_sort(C1, N)
selection_sort(C2, N)
print(*C1)
print(is_stable(C, C1))
print(*C2)
print(is_stable(C, C2))

