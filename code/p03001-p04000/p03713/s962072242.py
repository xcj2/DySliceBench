def yoko3(x, w, h):
    s1 = x * w
    h2 = (h-x)//2
    s2 = h2 * w
    s3 = (h - h2 - x) * w

    s = {s1, s2, s3}

    return max(s) - min(s)


def yoko1tate2(x, w, h):
    s1 = x * w
    w2 = w // 2
    s2 = (h-x)*w2
    s3 = (h-x)*(w-w2)

    s = {s1, s2, s3}

    return max(s) - min(s)


def solve():
    [H, W] = [int(x) for x in input().split()]

    ans = float("inf")
    ans = min(ans, min([yoko3(x, W, H) for x in range(H)]))
    ans = min(ans, min([yoko3(x, H, W) for x in range(W)]))
    ans = min(ans, min([yoko1tate2(x, W, H) for x in range(H)]))
    ans = min(ans, min([yoko1tate2(x, H, W) for x in range(W)]))

    return ans


if __name__ == '__main__':
    print(solve())