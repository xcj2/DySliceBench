import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = MI()

def med(arr):
    n = N
    arr.sort()
    if n % 2 == 0:
        return (arr[n//2-1] + arr[n//2]) / 2
    else:
        return arr[n//2]

meda = med(A)
medb = med(B)
if N % 2 != 0:
    print(int(max(meda, medb) - min(meda, medb) + 1))
else:
    print(int(2 * medb - 2 * meda + 1))