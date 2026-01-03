def main():
    S = input()

    editorial(S)


def editorial(S):
    """
    それぞれがそれ以外のprefixにならなければ良い
    """
    l = len(S)
    idx = 0
    ok = True
    rs = S[::-1]
    r7 = "dreamer"[::-1]
    r6 = "eraser"[::-1]
    r5_1 = "dream"[::-1]
    r5_2 = "erase"[::-1]

    while idx < l:
        if rs[idx:idx + 7] == r7:
            idx += 7
        elif rs[idx:idx + 6] == r6:
            idx += 6
        elif rs[idx:idx + 5] == r5_1 or \
                rs[idx:idx + 5] == r5_2:
            idx += 5
        else:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")


def RE(S):
    l = len(S)
    if _dfs(S, l, 0):
        print("YES")
    else:
        print("NO")


def _dfs(S, l, idx, pattern=0):
    # print(l, idx, pattern)
    if idx == l:
        return True

    if S[idx:idx + 7] == "dreamer":
        ok = _dfs(S, l, idx + 7, 1)
        if ok:
            return True
    if S[idx:idx + 6] == "eraser":
        ok = _dfs(S, l, idx + 6, 2)
        if ok:
            return True
    if S[idx:idx + 5] == "dream" or \
            S[idx:idx + 5] == "erase":
        ok = _dfs(S, l, idx + 5, 3)
        if ok:
            return True

    return False


def WA(S):
    l = len(S)
    idx = 0
    ok = True
    while idx < l:
        if S[idx:idx + 7] == "dreamer":
            idx += 7
        elif S[idx:idx + 6] == "eraser":
            idx += 6
        elif S[idx:idx + 5] == "dream" or \
                S[idx:idx + 5] == "erase":
            # 評価順番注意
            idx += 5
        else:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
