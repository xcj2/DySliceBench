import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))

acca = []

def merge(n, l, m, r):
    global acca
    cnt = 0
    n1, n2 = m - l, r - m
    la, ra = [], []
    for i in range(n1):
        la.append(acca[l + i])
    for i in range(n2):
        ra.append(acca[m + i])
    la.append(float("inf"))
    ra.append(float("inf"))
    i, j = 0, 0
    for k in range(l, r):
        if la[i] <= ra[j]:
            acca[k] = la[i]
            i += 1
        else:
            acca[k] = ra[j]
            j += 1
            cnt += n1 - i
    return cnt


def mergesort(n, l, r):
    if l + 1 < r:
        m = (l + r) // 2
        c1 = mergesort(n, l, m)
        c2 = mergesort(n, m, r)
        c3 = merge(n, l, m, r)
        return c1 + c2 + c3
    else:
        return 0


def main():
    global acca
    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a = [_a - k for _a in a]
    acca = [0 for i in range(n + 1)]
    for i, _a in enumerate(a):
        acca[i + 1] = acca[i] + _a

    print(n * (n + 1) // 2 - mergesort(n + 1, 0, n + 1))


if __name__ == '__main__':
    main()
