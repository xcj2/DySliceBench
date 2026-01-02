from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

N = ni()
A = nl()
if N%2 == 0:
    v1 = sum(A[::2])
    v2 = sum(A[1::2])
    M = max(v1, v2)
    l = 0
    for i in range(0, N, 2):
        v2 -= A[i+1]
        l += A[i]
        M = max(l + v2, M)
    print(M)
else:
    INF = 10**18
    DP = [[[-INF]*N for _ in range(3)] for _ in range(2)]
    DP[1][0][0] = A[0]
    DP[0][1][0] = 0
    for i in range(1, N):
        DP[1][0][i] = A[i] + DP[0][0][i-1]
        DP[1][1][i] = A[i] + DP[0][1][i-1]
        DP[1][2][i] = A[i] + DP[0][2][i-1]
        DP[0][0][i] = DP[1][0][i-1]
        DP[0][1][i] = max(DP[0][0][i-1], DP[1][1][i-1])
        DP[0][2][i] = max(DP[0][1][i-1], DP[1][2][i-1])

    print(max(DP[0][1][N-1], DP[1][1][N-1], DP[1][2][N-1]))


