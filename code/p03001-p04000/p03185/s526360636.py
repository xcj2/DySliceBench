# 追加クエリにおける直線の傾きが単調であり、最小値クエリにおけるxが単調である時の Convex-Hull Trick
# もっと言うと、今回は追加クエリの傾きが単調減少で、最小値クエリにおけるxが単調増加
# 参考 : http://satanic0258.hatenablog.com/entry/2016/08/16/181331

from collections import deque
deq = deque()

# 直線 l1, l2, l3のうち l2が不必要かどうか (不必要なら1, 必要なら0を返す)
def check(f1, f2, f3):
    return (f3[1] - f2[1]) * (f2[0] - f1[0]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

# f1(x)を返す
def f(f1, x):
    return f1[0] * x + f1[1]

# 直線 y = ax + b を追加
def add(a, b):
    # 直線 l1: deq[-2], l2: deq[-1], l3: (a, b)のうち, l2が不必要なら除くことを繰り返す
    while len(deq) >= 2 and check(deq[-2], deq[-1], (a, b)):
        deq.pop()
    deq.append((a, b))

#
def get(x):
    # 今回はクエリのxが単調増加であることを利用する
    # すると、あるクエリに置いて f1(x0) >= f2(x0)となればそれ以降(x > x0)でf1は最小となることはないので, f1を取り除く
    while len(deq) >= 2 and f(deq[0], x) >= f(deq[1], x):
        deq.popleft()
    # 上の操作後、deq の先頭が最小になるのでそれを返す
    return f(deq[0], x)


n, c = map(int, input().split())
h = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
add(-2 * h[0], h[0]**2 + dp[0])

for i in range(1, n):
    dp[i] = get(h[i]) + h[i]**2 + c
    add(-2 * h[i], h[i]**2 + dp[i])

print(dp[n-1])
