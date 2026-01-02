import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N, P = map(int, input().split())
    S = str(input())

    def main():
        if P == 2:
            res = 0
            for i in range(N):
                if int(S[N - 1 - i]) % 2 == 0:
                    res += N - i
        elif P == 5:
            res = 0
            for i in range(N):
                if int(S[N - 1 - i]) == 0 or int(S[N - 1 - i]) == 5:
                    res += N - i

        else:
            mods = [0] * P  # mods[i]はPで割ったあまりがiである連続部分列の個数
            tenfactor = 1
            mod = 0
            mods[mod] += 1

            for i in range(N):
                mod = (mod + int(S[N - i - 1]) * tenfactor) % P
                tenfactor = (tenfactor * 10) % P
                mods[mod] += 1

            res = 0
            for p in range(P):
                res += mods[p] * (mods[p] - 1) // 2

        return res

    print(main())


resolve()