import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from string import ascii_uppercase
    import bisect

    N, Q = map(int, readline().split())
    S = "*" + input()

    query = []
    for _ in range(Q):
        t, d = input().split()
        query.append([t, d])

    def judge(x):
        cur = x
        for t, d in query:
            if S[cur] == t:
                if d == "L":
                    cur -= 1
                else:
                    cur += 1
            if cur < 1:
                return -1
            if cur > N:
                return 1
        return 0

    def calc():
        l_ok = N + 1
        r_ok = 0

        l_ng = 0
        r_ng = N + 1

        # l_ok <= x <= r_ok
        # x <= l_ng, r_ng <= x

        while True:
            l_mid = (l_ok + l_ng) // 2
            r_mid = (r_ok + r_ng) // 2
            result = judge(l_mid)
            if result == -1:
                l_ng = max(l_ng, l_mid)
            elif result == 1:
                l_ok = l_mid
                r_ng = min(r_ng, l_mid)
            else:
                l_ok = min(l_ok, l_mid)
                r_ok = max(r_ok, l_mid)

            result = judge(r_mid)
            if result == -1:
                r_ok = r_mid
                l_ng = max(l_ng, r_mid)
            elif result == 1:
                r_ng = min(r_ng, r_mid)
            else:
                l_ok = min(l_ok, r_mid)
                r_ok = max(r_ok, r_mid)

            if l_ng + 1 == l_ok and r_ok + 1 == r_ng:
                return max(0, r_ok - l_ok + 1)
            if l_ng + 1 == r_ng:
                return 0

    print(calc())


if __name__ == '__main__':
    main()
