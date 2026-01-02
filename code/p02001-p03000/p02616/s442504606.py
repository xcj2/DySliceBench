from queue import PriorityQueue
import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


mod = 10**9+7


def prod(l):
    ret = 1
    for e in l:
        e %= mod
        ret = (ret*e) % mod

    return ret


def main():
    n, k = geta(int)
    a = list(geta(int))

    p, n, z = [], [], 0
    for ai in a:
        if ai > 0:
            p.append(ai)
        elif ai < 0:
            n.append(-ai)
        else:
            z += 1

    ans = 1
    p.sort()
    n.sort()
    if k & 1 == 1:
        if len(p) == 0:
            if z > 0:
                print(0)
                exit()
            else:
                print(-prod(n[0:k]) % mod)
                exit()
        else:
            k -= 1
            ans = p.pop() % mod

    if len(p) + len(n) < k:
        print(0)
        exit()

    if len(n) & 1 == 1 and (len(p) + len(n) == k):
        if z > 0:
            print(0)
            exit()
        else:
            print(-prod(p) * prod(n) % mod)
            exit()

    q = []

    n = n[::-1]
    for i in range(len(n)//2):
        q.append(n[2*i]*n[2*i+1])

    p = p[::-1]
    for i in range(len(p)//2):
        q.append(p[2*i]*p[2*i+1])

    q.sort(reverse=True)

    ans = ans * (prod(q[:k//2])) % mod

    print(ans % mod)


if __name__ == "__main__":
    main()
