from collections import Counter
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()

N, Q = tuple(li())
S = ns()
ops = []
for i in range(Q):
    ops.append(tuple(ls()))

head, tail = 0, N-1
while(ops):
    cur = ops.pop()
    if cur[1] == 'L' and head <N:
        if S[head] == cur[0]:
            head += 1
        if tail <= N-2 and S[tail + 1] == cur[0]:
            tail = min(tail + 1, N-1)
    elif cur[1] == 'R' and tail >= 0:
        if S[tail] == cur[0]:
            tail -= 1
        if head >= 1 and S[head - 1] == cur[0]:
            head = max(0, head-1)
alive = tail - head + 1
# print("tail:{}, head:{}".format(tail, head))
print(max(alive, 0))
