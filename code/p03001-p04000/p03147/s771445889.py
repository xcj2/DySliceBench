def find_zeros(a):
    res = []
    for i in range(len(a)):
        if a[i] == 0:
            res.append(i)
    return res


def solve():
    N = input()
    h = [int(n) for n in input().split()]

    cnt = 0
    while sum(h) != 0:
        idx_zeros = find_zeros(h)
        idx_zeros = [-1] + idx_zeros + [len(h)]
        for l, r in zip(idx_zeros[:-1], idx_zeros[1:]):
            for i in range(l+1,r):
                h[i] -= 1
            if l+1<r:
                cnt += 1
    return cnt 


def main():
    ans = solve()
    print(ans)


if __name__ == '__main__':
    main()
