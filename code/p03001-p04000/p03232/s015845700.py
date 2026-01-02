import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b
mod = 7 + 10 ** 9
  
def solve():
    N = int(single_input())
    A = [int(a) for a in line_input()]
    factorial_N = 1
    accumulated_sum_nrev = [0] * (N + 1)
    for i in range(1, N+1):
        accumulated_sum_nrev[i] = accumulated_sum_nrev[i-1] + pow(i, mod - 2, mod)
        factorial_N *= i
        factorial_N %= mod
    ans = 0
    for i in range(N):
        ans += A[i] * factorial_N * (accumulated_sum_nrev[i+1] + accumulated_sum_nrev[N- i] - 1) % mod
        ans %= mod
    return ans
    

if __name__ == "__main__":
    print(solve())