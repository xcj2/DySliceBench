import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

# 入力
n, k = li()
v = list(li())

# 個数m決め打ち
ans = 0
for m in range(n+1):
    rest = k
    rest -= m

    if rest < 0:
        continue

    # 左からi個、右からm-i個
    for i in range(m+1):
        a = v[:i] + v[n-m+i:]
        a.sort()
        suma = sum(a)

        # kを超えないようにマイナスを詰める
        for j in range(rest):
            if j >= len(a):
                break

            if a[j] < 0:
                suma += abs(a[j])
            else:
                break

        ans = max(ans, suma)

print(ans)