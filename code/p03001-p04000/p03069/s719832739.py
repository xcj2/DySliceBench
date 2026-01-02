from collections import Counter
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
def ns(): return stdin.readline().rstrip()
N = ii()
S = ns()
bs = [0] * (N + 1)
ws = [0] * (N + 1)
total = float("inf")
left_b = 0
right_w = 0
for i, s in enumerate(S):
    if s == "#":
        left_b += 1
    bs[i + 1] = left_b
for i in reversed(range(N)):
    if S[i] == ".":
        right_w += 1
    ws[i] = right_w

for i in range(N):
    total = min(total, ws[i+1] + bs[i])

print(total)
