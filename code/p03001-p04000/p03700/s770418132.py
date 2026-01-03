import math
def bsearch_int(init_ng, init_ok, cond):
    ng = init_ng
    ok = init_ok
    while(abs(ok - ng) > 1):
        mid = math.floor(abs(ok + ng)/2)
        if cond(mid):
            ok = mid
        else:
            ng = mid
    return ok

def condition(cnt, N, A, B, hs):
    basedmg = B*cnt
    diff = A - B
    diffcnt = 0
    for h in hs:
        if h < basedmg:
            break
        else:
            diffcnt += math.ceil((h-basedmg)/diff)
    if diffcnt > cnt:
        return False
    else:
        return True

import functools
def resolve():
    N, A, B = list(map(int, input().split(" ")))
    hs = [int(input()) for i in range(N)]
    hs.sort(reverse=True)
    print(bsearch_int(0, math.ceil(hs[0]/B), functools.partial(condition, N=N, A=A, B=B, hs=hs)))


if __name__ == '__main__':
    resolve()