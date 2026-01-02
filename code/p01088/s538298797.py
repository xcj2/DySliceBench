from copy import deepcopy
from operator import itemgetter

def buy(p, cr):
    cnt, rem = cr
    r1000 = p % 1000
    r500 = p % 500
    m500 = 500 - r500
    m1000 = 1000 - r1000
    if r1000 == 0:
        if rem < 500:
            return ((cnt, rem),)
        else:
            return ((cnt+1, rem-500),)
    elif r1000 == 500:
        return ((cnt+1, rem),)
    elif r1000 < 500:
        return ((cnt+1, rem + m500), (cnt, rem + m1000))
    else:
        if rem - r500 >= 0:
            return ((cnt+1, rem - r500),)
        else:
            return ((cnt, rem + m500),)

INF = 10**20

def solve(plist):
    dp = {
        (0, 0): 0
    }
    for p in plist:
        ndp = {}
        for cr in list(dp.keys()):
            for ncr in buy(p, cr):
                ndp[ncr] = min(dp[cr] + p, dp.get(ncr, INF))

        dp.update(ndp)
        ndp = {}
        cc = -1
        mp = INF
        for c, r in sorted(dp.keys(), reverse=True):
            pp = dp[(c, r)]
            if cc != c:
                mp = INF
                cc = c
            if mp > pp:
                ndp[(c, r)] = pp
                mp = pp
        dp = ndp

    cplist = ((t[0][0], t[1]) for t in dp.items())
    return sorted(sorted(cplist, key=itemgetter(1)),
                  key=itemgetter(0), reverse=True)[0]

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        plist = [int(input().strip()) for _ in range(n)]
        print(" ".join(str(i) for i in solve(plist)))

if __name__ == '__main__':
    main()

