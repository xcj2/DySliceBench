import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def gcd(a, b):
    # greatest common divisor
    while b > 0:
        a, b = b, a % b

    return a


MOD = 10**9 + 7


def POW(a, p):
    if a == 1 or p == 0:
        return 1

    if p == 1:
        return a
    else:
        return (POW(a, p // 2)**2 * (a**(p % 2))) % MOD


def ShinKosuu(k, kosuu, shinkosuu):
    ret = kosuu[k]
    for t in range(k * 2, K + 1, k):
        ret -= shinkosuu[t]
    return ret


def main():

    ans = 0
    kosuu = [0] * (K + 1)
    shinkosuu = [0] * (K + 1)
    for k in range(K, 0, -1):
        kosuu[k] = POW(K // k, N)
        shinkosuu[k] = ShinKosuu(k, kosuu, shinkosuu)
        ans = (ans + k * shinkosuu[k]) % MOD
    # print(kosuu)

    print(ans)


if __name__ == '__main__':
    N, K = inpl()
    main()
