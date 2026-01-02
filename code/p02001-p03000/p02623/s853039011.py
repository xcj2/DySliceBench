import sys
import heapq
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M, K = ZZ()
    A = ZZ()
    B = ZZ()
    k = 0
    for i in range(N):
        if k + A[i] <= K: k += A[i]
        else: break
    else: i += 1
    ans = i
    for j in range(M):
        if k + B[j] <= K: k += B[j]
        else: break
    else: j += 1
    ans += j
    for ii in range(1, i+1):
        k -= A[i-ii]
        while j < M and k + B[j] <= K:
            k += B[j]
            j += 1
        ans = max(ans, i+j-ii)
    print(ans)

    return

if __name__ == '__main__':
    main()
