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
    ks = [[int(i) for i in line_input()] for j in range(M)]
    p = [int(i) for i in line_input()]
    ans = 0
    for i in range(2 ** N):
        onoff = str(format(i, "b").zfill(N))
        for m in range(M):
            onnum = 0
            for k in ks[m][1:]:
                if onoff[k-1] == "1": onnum += 1
            if onnum % 2 != p[m]: break
        else: ans += 1
    print(ans)
        
    return 0
  
if __name__ == "__main__":
    solve()