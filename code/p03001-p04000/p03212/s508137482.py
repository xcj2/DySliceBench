def main():
    """
    1 <= N  <= 10^9

    七五三数とは以下の条件を満たす正の整数
    十進法で表記したとき、
    数字 7, 5, 3 がそれぞれ 1回以上現れ、これら以外の数字は現れない
    """
    N = int(input())

    # ans = f(N)
    ans = editorial(N)
    ans2 = editorial_movie(N)
    assert ans == ans2
    print(ans)


def editorial(N):
    def dfs(s):
        if int(s) > N:
            return 0

        ret = all(s.count(c) for c in "753")
        ret = int(ret)

        for c in "753":
            ret += dfs(s + c)

        return ret

    ans = dfs("0")
    return ans


def editorial_movie(N):
    def dfs(x):
        if x > N:
            return 0

        s = str(x)
        ret = all(s.count(c) for c in "753")
        ret = int(ret)

        for c in [7,5,3]:
            ret += dfs(x * 10 + c)

        return ret

    ans = dfs(0)
    return ans

if __name__ == '__main__':
    main()
