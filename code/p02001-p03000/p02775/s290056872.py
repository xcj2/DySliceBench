#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: str):
    # 下の桁から貪欲？
    N = "0" + N
    ans = 0
    kuriagari = 0
    for i in reversed(range(len(N))):
        n = int(N[i])
        if kuriagari == 1:
            kuriagari = 0
            n += 1
        if 0 <= n <= 4:
            ans += n
        elif n == 5:
            # print("上の桁を見て決める")
            k = i-1
            if 0 <= int(N[k]) <= 4:
                # print("桁上がらない")
                ans += 5
            else:
                # print("桁上がる")
                ans += 5
                kuriagari = 1
        else:
            ans += 10 - n
            kuriagari = 1
        # print("現状", ans, kuriagari)
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = next(tokens)
    N = str(a)  # type: str
    solve(N)


if __name__ == '__main__':
    main()
