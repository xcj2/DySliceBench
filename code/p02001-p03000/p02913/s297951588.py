def z_algo(s):
    N = len(s)
    A = [0]*N
    i = 1; j = 0
    A[0] = N
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while N-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k

    # 自身は含まない
    for i in range(N):
        A[i] = min(A[i],i)
    #
    return A

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N = I()
S = str(input())
cur = int(0)
ans = int(0)
lenC = []

for i in range(N):
#    print(z_algo(S[i:]))
    lenC.append(max(z_algo(S[i:])))

#print(lenC)
ans = max(lenC)
print(ans)