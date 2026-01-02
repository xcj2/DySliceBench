def main():
    N, A, B, C = map(int, input().split())
    ls = [int(input()) for _ in range(N)]

    ans = editorial(N, A, B, C, ls)
    print(ans)


def editorial(N, A, B, C, ls):
    def dfs(cur, a, b, c):
        if cur == N:
            if min([a, b, c]) > 0:
                # 使わなくて足りない/使いすぎて超過している分は差引すればいい
                tmp = abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                tmp = float("inf")
            # print(tmp, a, b, c, sep="\t")
            return tmp

        # 使うか使わないか,合成パターンを試す
        d = ls[cur]
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + d, b, c) + 10
        ret2 = dfs(cur + 1, a, b + d, c) + 10
        ret3 = dfs(cur + 1, a, b, c + d) + 10

        return min([ret0, ret1, ret2, ret3])

    ans = dfs(0, 0, 0, 0)
    return ans


if __name__ == '__main__':
    main()
