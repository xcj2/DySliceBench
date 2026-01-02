import copy

def bubble(N, A):
    for i in range(N - 1):
        for j in reversed(range(1, N)):
            if A[j - 1][1] > A[j][1]:
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp

def select(N, A):
    for i in range(N):
        min = i
        for j in range(i, N):
            if A[min][1] > A[j][1]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp

def st(B, S):
    for i in range(N):
        if B[i] != S[i]:
            return False
    return True

N = int(input())
#カード入力
S = [i for i in input().split()]
B = copy.deepcopy(S)

bubble(N, B)
select(N, S)

print(" ".join(B))
print("Stable")
print(" ".join(S))
if st(B, S) == True:
    print("Stable")
else:
    print("Not stable")
