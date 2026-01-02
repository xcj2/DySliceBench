import sys


def _s(): return sys.stdin.readline().strip()


def _i(): return int(sys.stdin.readline().strip())


def main():
    n = _i()
    s = _s()
    m = s.count("1")
    arr = list(range(max(1, m-1), m+2))
    d1 = {}
    for ai in arr:
        d1[ai] = [1 % ai]
        for i in range(n-1):
            d1[ai].append((2*d1[ai][-1]) % ai)

    d2 = {ai: 0 for ai in arr}
    for ai in arr:
        for i, c in enumerate(reversed(s)):
            if c == "1":
                d2[ai] = (d2[ai] + d1[ai][i]) % ai

    lst = [0] * (n+1)
    for i in range(1, n+1):
        t = i % bin(i)[2:].count("1")
        lst[i] = 1 + lst[t]

    i = n
    for c in s:
        i -= 1
        if c == "1":
            m1 = m - 1
            if m1 == 0:
                print(0)
                continue
            else:
                t = (d2[m1] - d1[m1][i]) % m1
        else:
            m1 = m + 1
            t = (d2[m1] + d1[m1][i]) % m1
        print(lst[t] + 1)


if __name__ == "__main__":
    main()
