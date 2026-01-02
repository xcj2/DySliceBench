def z_algo(s):
    N = len(s)
    A = [0]*N
    i = 1; j = 0
    l = len(s)
    A[0] = l
    B = [0]*N
    while i < l:
        while i+j < l and s[j] == s[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k

    # 自身は含まない
    for i in range(N):
        B[i] = i
    #
    for i in range(N):
        A[i] = min(A[i],i)
#    print(B)
#    A[0] = 0
    return A

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = []

N = I()
S = str(input())
cur = int(0)
ans = int(0)
lenC = []

for i in range(N):
#    print(z_algo(S[i:]))
    lenC.append(max(z_algo(S[i:])))

#print(lenC)
ans = min(max(lenC),N//2)
print(ans)
