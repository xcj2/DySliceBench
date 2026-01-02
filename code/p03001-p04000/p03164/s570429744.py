from heapq import heappop, heappush
from operator import itemgetter


def branchAndBound(N: int, M: int, V: list, W: list, R: list) -> int:
    def upperbound(w, v, i):
        rest = M - w
        _v = v
        for j in range(i + 1, N):
            if W[j] >= rest:
                rest -= W[j]
                v += V[j]
                _v = v
            else:
                _v += R[j] * rest
                break
        return v, _v

    prov, tmp = upperbound(0, 0, -1)
    h = [(tmp, W[0], V[0] * (W[0] >= M), 0), (upperbound(0, 0, 0)[1], 0, 0, 0)]
    while h:
        _v, w, v, cur = heappop(h)
        if _v > prov or cur == N - 1:
            continue
        nxtw, nxtv = w + W[cur + 1], v + V[cur + 1]
        if nxtw >= M:
            heappush(h, (_v, nxtw, nxtv, cur + 1))
        _prov, ub = upperbound(w, v, cur)
        if _prov < prov:
            prov = _prov
        if ub < prov:
            heappush(h, (ub, w, v, cur + 1))
    return -prov


def main():
    N, M, *L = map(int, open(0).read().split())
    t = [(v, w, v / w) for w, v in zip(*[iter(L)] * 2)]
    t.sort(key=itemgetter(2), reverse=True)
    V, W, R = [], [], []
    for v, w, r in t:
        V += [-v]
        W += [-w]
        R += [r]
    ans = branchAndBound(N, -M, V, W, R)
    print(ans)
    
if __name__=="__main__":main()
