import sys
import heapq


def _i(): return int(sys.stdin.readline().strip())


def _ia(): return map(int, sys.stdin.readline().strip().split())


def reward(n, d):
    s = []
    for i in range(n):
        for item in d.get(i, []):
            heapq.heappush(s, item)
        for _ in range(len(s), i+1, -1):
            _ = heapq.heappop(s)
    return sum(s)


def test():
    n = _i()
    ll, rr = {}, {}
    mn = ln = rn = 0
    for i in range(n):
        k, l, r = _ia()
        mn += min(l, r)
        if l >= r:
            ll[k-1] = ll.get(k-1, []) + [l-r]
            ln += 1
        else:
            rr[n-k-1] = rr.get(n-k-1, []) + [r-l]
            rn += 1

    return mn + reward(n, ll) + reward(n, rr)


def main():
    t = _i()
    ret = [test() for _ in range(t)]
    return "\n".join(map(str, ret))


if __name__ == "__main__":
    print(main())
