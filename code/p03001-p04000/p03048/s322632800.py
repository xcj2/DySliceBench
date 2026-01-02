import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b
  
def solve():
    R, G, B, N = map(int, line_input())
    ans = 0
    for r in range(N // R + 1):
        left = N - r * R
        for g in range(left // G + 1):
            if (left - g * G) % B == 0: ans += 1
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()