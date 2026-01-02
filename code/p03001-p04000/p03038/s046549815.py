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
    A = [int(a) for a in line_input()]
    change = [None] * M
    for i in range(M):
        b, c = map(int, line_input())
        change[i] = [c, b]
    A.sort()
    change.sort(reverse = True)

    sum = 0
    index = 0
    for c, b in change:
        bleft = b
        while bleft > 0:
            if c > A[index]:
                sum += c
                index += 1
                bleft -= 1
                if index == N: break
            else: break
        if index == N: break
    if index < N:
        for i in range(index, N):
            sum += A[i]
    print(sum)

    return 0
  
if __name__ == "__main__":
    solve()