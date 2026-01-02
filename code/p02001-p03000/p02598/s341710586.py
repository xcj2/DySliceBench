#create date: 2020-08-03 14:18

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def cut(a, l):
    res = 0
    for ai in a:
        res += max(0, (ai-1)//l)
        #print(ai, max(0, (ai-1)//l), res)
    return res


def main():
    n, k = na()
    a = na()
    ansl, ansr = 0, 10**9
    while ansl + 1 < ansr:
        now = (ansl + ansr) // 2
        #print(ansl, ansr, now, cut(a, now))
        if cut(a, now) <= k:
            ansr = now
        else:
            ansl = now
    print(ansr)

if __name__ == "__main__":
    main()