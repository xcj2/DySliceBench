def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]

    # ans = f(H, W, a)
    # ans = T(H, W, a)
    ans = editorial(H, W, a)
    for x in ans:
        print(*x, sep="")


def editorial(H, W, a):
    # 出力する部分の記憶
    row = [False] * H
    col = [False] * W

    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                row[i] = True
                col[j] = True

    ans = []
    for i in range(H):
        if not row[i]:
            continue

        line = []
        for j in range(W):
            if col[j]:
                line.append(a[i][j])
        ans.append(line)

    if not ans:
        return [[]]

    return ans


def T(H, W, a):
    """
    転置
    本番ではバグらせるのを恐れて愚直に実装した
    """
    b = []
    c = []
    for line in a:
        if len(line) != line.count("."):
            b.append(line)

    for line in zip(*b):
        if len(line) != line.count("."):
            c.append(line)

    if not c:
        return [[]]

    return list(zip(*c))


def f(H, W, a):
    b = []
    for line in a:
        if len(line) != line.count("."):
            b.append(line)

    if not b:
        return [[]]

    idxes = []
    for x in range(len(a[0])):
        y = sum(1 for i in range(len(b)) if b[i][x] == ".")
        if y != len(b):
            idxes.append(x)

    if not idxes:
        return [[]]

    ans = []
    for i in range(len(b)):
        line = []
        for j in range(len(a[0])):
            if j in idxes:
                line.append(b[i][j])
        ans.append(line)

    return ans


if __name__ == '__main__':
    main()
