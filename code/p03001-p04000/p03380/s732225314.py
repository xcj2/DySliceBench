dp_t = dict()
dp_p = dict()


def main():
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort(reverse=True)
    t = a[0] // 2
    p = a[-1]
    if n == 2:
        print("%d %d" % (a[0], a[1]))
        return
    i = 1
    while a[i] > t:
        i += 1
        if i >= n:
            i -= 1
            break
    if abs(a[i - 1] - t) > abs(a[i] - t):
        p = a[i]
    else:
        p = a[i - 1]
    print("%d %d" % (a[0], p))


def main1():
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort(reverse=True)
    max_comb = (0, 0)
    max_num = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            c = comb(a[i], a[j])
            if max_num < c:
                max_num = c
                max_comb = (a[i], a[j])
    print("%d %d" % max_comb)


def comb(n, r):
    t = 1
    if n in dp_t:
        t = dp_t[n]
    else:
        t = compute_kai(n)
    p = 1
    if (n, r) in dp_p:
        p = dp_p[(n, r)]
    else:
        pr = 1
        if r in dp_t:
            pr = dp_t[r]
        else:
            pr = compute_kai(r)
        if n - r in dp_t:
            p = dp_t[n - r]
        else:
            p = compute_kai(n -r)
        p *= pr
        dp_p[(n, r)] = p
    return t // p


def compute_kai(n):
    if n in dp_t:
        return dp_t[n]
    else:
        t = 1
        for i in range(n):
            t *= (n - i)
        dp_t[n] = t
        return t


if __name__ == '__main__':
    main()
