def BubbleSort(C_B, N):
    for i in range(N):
        for j in range(N-1,i,-1):
            if int(C_B[j][1]) < int(C_B[j-1][1]) :
                C_B[j], C_B[j-1] = C_B[j-1], C_B[j]
    return C_B

def SelectionSort(C_S, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(C_S[j][1]) < int(C_S[minj][1]):
                minj = j
        C_S[i], C_S[minj] = C_S[minj], C_S[i]
    return C_S

def J(C, C_):
    for i in range(1,len(C_)):
        if int(C_[i-1][1]) == int(C_[i][1]):
            p = C.index(C_[i-1])
            q = C.index(C_[i])
            if q<p:
                return 'Not stable'
    return 'Stable'

N = int(input())
C = list(input().split())
C_B = C.copy()
C_S = C.copy()
CB = BubbleSort(C_B, N)
CS = SelectionSort(C_S, N)

for i in range(len(CB)):
    if i==len(CB)-1:
        print(CB[i])
    else:
        print(CB[i],end=' ')
print(J(C, CB))
for i in range(len(CS)):
    if i==len(CS)-1:
        print(CS[i])
    else:
        print(CS[i],end=' ')
print(J(C, CS))
