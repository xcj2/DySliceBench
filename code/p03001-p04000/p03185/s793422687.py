import sys
input = sys.stdin.readline
N, C = map(int, input().split())
a = list(map(int, input().split()))

from collections import deque
deq = deque()
def check(f1, f2, f3):
    return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
def f(f1, x):
    return f1[0]*x + f1[1]

# add f_i(x) = a*x + b
def add_line(a, b):
    f1 = (a, b)
    while len(deq) >= 2 and check(deq[-2], deq[-1], f1):
        deq.pop()
    deq.append(f1)

# min f_i(x)
def query(x):
    while len(deq) >= 2 and f(deq[0], x) >= f(deq[1], x):
        deq.popleft()
    return f(deq[0], x)

add_line(-2 * a[0], a[0] ** 2 + C)
dp = [0] * N
for i in range(1, N):
  x = query(a[i]) + a[i] ** 2
  add_line(-2 * a[i], x + C + a[i] ** 2)
  dp[i] = x
print(dp[-1])