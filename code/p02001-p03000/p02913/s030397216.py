import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()


def Z_algorithm(S):
    N = len(S)
    A = [0]*N
    A[0] = N
    i,j = 1,0
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        if j == 0:
            i += 1
            continue
        # S[0:j] == S[i:i+j] となっている
        A[i] = j
        k = 1
        while i+k < N and k+A[k] < j:
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    return A


ans = 0
for i in range(N):
    A = Z_algorithm(S)
    for j in range(N-i):
        if A[j] <= j:
            ans = max(ans,A[j])
    del S[0]

print(ans)
