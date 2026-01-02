def update(bin_tree, x, y, n):
    i = n - 1 + x
    bin_tree[i] = y

    while i > 0:
        i = int((i - 1) / 2)
        bin_tree[i] = min(bin_tree[2*i+1], bin_tree[2*i+2])


def find(bin_tree, x, y, k, l, r):
    if r <= x or y <= l:
        return 2**31-1
    elif x <= l and r <= y:
        return bin_tree[k]
    else:
        vl = find(bin_tree, x, y, 2 * k + 1, l, int((l + r) / 2))
        vr = find(bin_tree, x, y, 2 * k + 2, int((l + r) / 2), r)
        return min(vl, vr)


def main():
    [n, q] = [int(num) for num in input().split()]

    m = 1
    while m < n:
        m *= 2

    bin_tree = [2**31-1 for _ in range(2*m-1)]

    for i in range(q):
        # print(bin_tree)
        [com, x, y] = [int(num) for num in input().split()]

        if com == 0:
            update(bin_tree, x, y, m)
        else:
            print(find(bin_tree, x, y+1, 0, 0, m))


if __name__ == '__main__':
    main()

