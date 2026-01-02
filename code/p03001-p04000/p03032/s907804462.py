import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    N, K = map(int, line_input())
    V = [int(v) for v in line_input()]
    maxpoint = 0
    for i in range(N + 1):
        for j in range(N - i + 1):
            if i + j <= min(N, K):
                trash = []
                heapq.heapify(trash)
                point = sum(V[:i])
                for k in range(j):
                    point += V[-1 - k]
                    heapq.heappush(trash, V[-1-k])
                for a in range(i):
                    heapq.heappush(trash, V[a])
                count = 0
                while trash and count < K - (i + j):
                    bye = heapq.heappop(trash)
                    count += 1
                    if bye > 0: break
                    else: 
                        point -= bye
                maxpoint = max(maxpoint, point)
    print(maxpoint)
    return 0
  
if __name__ == "__main__":
    solve()