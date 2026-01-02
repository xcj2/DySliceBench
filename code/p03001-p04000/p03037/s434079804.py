import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    N, M = map(int, line_input())
    gate = [0 for n in range(N+1)]
    for i in range(M):
        l, r = map(int, line_input())
        gate[l-1] += 1
        gate[r] -= 1
    ans = (1 if gate[0] == M else 0)
    for i in range(1, N):
        gate[i] = gate[i] + gate[i-1]
        if gate[i] == M: ans += 1
    print(ans)
    return 0
  
if __name__ == "__main__":
    solve()