# AGC026c
ans = 0


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    n = int(input())
    s = input()[:-1]
    sLatter = s[n:][::-1]

    d = dict()

    def dfs1(i, sR, sB):
        if i == n:
            if not (sR, sB[::-1]) in d:
                d[(sR, sB[::-1])] = 0
            d[(sR, sB[::-1])] += 1
            return
        dfs1(i + 1, sR + s[i], sB)
        dfs1(i + 1, sR, sB + s[i])

    dfs1(0, '', '')
    # print(d)

    def dfs2(i, sR, sB):
        if i == n:
            if (sR, sB[::-1]) in d:
                global ans
                ans += d[(sR, sB[::-1])]
            return
        dfs2(i + 1, sR + sLatter[i], sB)
        dfs2(i + 1, sR, sB + sLatter[i])

    dfs2(0, '', '')
    print(ans)


if __name__ == '__main__':
    main()
