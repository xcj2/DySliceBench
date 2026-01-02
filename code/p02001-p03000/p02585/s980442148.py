import sys


def _ia(): return map(int, sys.stdin.readline().strip().split())


def calc(arr, k):
    s = sum(arr)
    n = len(arr)
    kp = k % n if s > 0 else k
    if kp == 0:
        kp = n

    ll = min(kp, n)
    cm = max(arr)
    for i in range(n):
        cn = 0
        for ki in range(i, i+ll):
            cn += arr[ki % n]
            cm = max(cn, cm)

    if s > 0:
        return s * ((k-1)//n) + cm
    else:
        return cm


def main():
    n, k = _ia()
    p = list(map(lambda x: x-1, _ia()))
    c = list(_ia())

    f = [False] * n
    g = []
    for idx in range(n):
        if f[idx]:
            continue

        nxt = idx
        tmp = [c[nxt]]
        f[nxt] = True

        for _ in range(n):
            nxt = p[nxt]
            if nxt == idx:
                break
            tmp.append(c[nxt])
            f[nxt] = True

        g.append(tmp)

    return max(calc(gi, k) for gi in g)


if __name__ == "__main__":
    print(main())
