def ss(s):
    # 文字ソート
    res = s[0]
    for i in s[1:]:
        flg = False
        for j, e in enumerate(res):
            if e > i:
                res = res[:j] + i + res[j:]
                flg = True
                break

        if not flg:
            res += i
    return res


def poe(n):
    return sum([i - 1 for i in range(2, n + 1)])


def main():
    n = int(input())
    slist = {}
    for i in range(n):
        s = ss(input())
        if s in slist:
            slist[s] += 1
        else:
            slist[s] = 1

    ans = 0
    for k, v in slist.items():
        a = poe(v)
        ans += a
    print(ans)


if __name__ == '__main__':
    main()
