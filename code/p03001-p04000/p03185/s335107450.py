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

N,C=map(int,input().split())
h=list(map(int,input().split()))
dp=[0]*N
dp[-1]=0
add_line(2*h[-1],h[-1]**2)
for i in range(N-2,-1,-1):
    dp[i]=h[i]**2+C+query(-h[i])
    add_line(2*h[i],h[i]**2+dp[i])

print(dp[0])