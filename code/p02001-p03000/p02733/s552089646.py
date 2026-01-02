# https://atcoder.jp/contests/abc159/submissions/11108540

def main():
    def calc(group):
        ret = max(group)
        ctr = [0] * H
        for c in range(W):
            need_cut = False
            for r, g in enumerate(group):
                ctr[g] += s[r][c]
                if ctr[g] > K:
                    need_cut = True
                    break

            if need_cut:
                ctr = [0] * H
                ret += 1
                for r, g in enumerate(group):
                    ctr[g] += s[r][c]
                    if ctr[g] > K:
                        return H * W
                continue
        return ret

    def gen():
        from itertools import accumulate, product

        for prod in product(range(2), repeat=H - 1):
            group = [0]
            group.extend(accumulate(prod))
            yield calc(group)

    H, W, K = map(int, input().split())
    s = []
    for _ in range(H):
        *row, = map(int, input())
        s.append(row)

    ret = min(gen())
    print(ret)


if __name__ == '__main__':
    main()
