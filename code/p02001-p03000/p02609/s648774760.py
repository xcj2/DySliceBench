import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


def divide(X, s):
    ans = 0
    for i in X:
        ans *= 2
        i = int(i)
        ans += i
        ans = ans % s
    return ans


def popcount(n):
    ans = 0
    while(n > 0):
        ans += n & 1
        n = n >> 1
    return ans


def count(n):
    cnt = 1
    while(n > 0):
        n = n % popcount(n)
        cnt += 1
    return cnt


N = ni()
X = ns()

cnt = X.count("1")

if cnt == 0:
    for i in range(N):
        print(1)
    exit()


cnt_plus = cnt + 1
cnt_minus = cnt - 1
p = 1
m = 1
p_array = []
if cnt_minus > 0:
    m_array = []
for i in range(N):
    p_array.append(p)
    p = p * 2 % cnt_plus
    if cnt_minus > 0:
        m_array.append(m)
        m = m * 2 % cnt_minus

plus_first = divide(X, cnt_plus)
if cnt_minus > 0:
    minus_first = divide(X, cnt_minus)


for i, x in enumerate(X):
    if x == "0":
        first = (plus_first + p_array[-(i+1)]) % cnt_plus
        print(count(first))
    else:
        if cnt_minus == 0:
            print(0)
        else:
            first = (minus_first - m_array[-(i+1)]) % cnt_minus
            print(count(first))
