import sys
from operator import itemgetter


def _s(): return sys.stdin.readline().strip()


def _i(): return int(sys.stdin.readline().strip())


def parse(s):
    l, r = 0, 0
    for c in s:
        if c == '(':
            r += 1
        else:
            if r > 0:
                r -= 1
            else:
                l += 1
    return (l, r)


def main():
    n = _i()
    p = list(filter(lambda x: x != (0, 0), [parse(_s()) for _ in range(n)]))
    u, d = [], []
    for l, r in p:
        u.append((l, r)) if l <= r else d.append((l, r))
    u.sort(key=itemgetter(0))
    d.sort(key=itemgetter(1), reverse=True)
    r = 0
    for ll, rr in u+d:
        if ll > r:
            return 'No'
        r += (rr - ll)

    return 'Yes' if r == 0 else 'No'


if __name__ == "__main__":
    print(main())
