import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()
a_array = na()

mod = 10 ** 9 + 7

aa = []

for a in a_array:
    if a >= 0:
        aa.append([a, 1])
    else:
        aa.append([abs(a), 0])

aa = sorted(aa, key=lambda x: - (x[0]+0.1*x[1]))

minus_count = 0

last_plus = [0, 0]
last_minus = [0, 0]

for i in range(K):
    v, f = aa[i]
    if f == 0:
        minus_count += 1
        last_minus = [v, i]
    else:
        last_plus = [v, i]

ans = 1

if minus_count % 2 == 0:
    for i in range(K):
        ans = (ans * aa[i][0]) % mod
    print(ans)
    exit()
else:
    if aa[K-1][0] == 0:
        print(0)
        exit()
    plus_ok = 0
    minus_ok = 0
    change_plus = [-1, 0]
    change_minus = [0, 0]
    for i in range(K, N):
        v, f = aa[i]
        if plus_ok == 0 and minus_count != 0 and f == 1:
            plus_ok = 1
            change_plus = [v, i]
        elif minus_ok == 0 and minus_count != K and f == 0:
            minus_ok = 1
            change_minus = [v, i]
        if minus_ok == 1 and plus_ok == 1:
            break

    if minus_ok == 0 and plus_ok == 0:
        for i in range(N-1, N-K-1, -1):
            ans = (ans * aa[i][0]) % mod
        if ans == 0:
            print(0)
        else:
            print(mod - ans)
        exit()

    D = last_plus[0] * change_plus[0] - last_minus[0] * change_minus[0]

    # print(change_plus, change_minus, last_plus, last_minus)

    ans = 1

    if D >= 0:
        for i in range(K):
            if i != last_minus[1]:
                ans = (ans * aa[i][0]) % mod
        ans = ans * aa[change_plus[1]][0] % mod
        print(ans)
    else:
        for i in range(K):
            if i != last_plus[1]:
                ans = (ans * aa[i][0]) % mod
        ans = ans * aa[change_minus[1]][0] % mod
        print(ans)
