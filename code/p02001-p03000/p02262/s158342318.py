#!/usr/bin/env python3

def construct_gs(n):
    gs = []
    g = 1
    while g <= n:
        gs.append(g)
        g = 3 * g + 1
    return gs[::-1]


def shell_sort(xs, n):
    global cnt
    cnt = 0
    gs = construct_gs(n)
    m = len(gs)
    def insertion_sort(g):
        global cnt
        for i in range(g, n):
            v = xs[i]
            j = i - g
            while j >= 0 and xs[j] > v:
                xs[j + g] = xs[j]
                j = j - g
                cnt += 1
            xs[j + g] = v
    for g in gs:
        insertion_sort(g)
    return m, gs, cnt, xs


def main():
    n = int(input())
    xs = [int(input()) for _ in range(n)]
    m, gs, cnt, xs = shell_sort(xs, n)
    print(m)
    print(" ".join(map(str, gs)))
    print(cnt)
    for x in xs:
        print(x)


if __name__ == '__main__':
    main()