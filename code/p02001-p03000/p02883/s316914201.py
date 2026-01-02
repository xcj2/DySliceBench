import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, K = ZZ()
    A = sorted(ZZ(), reverse=True)
    F = sorted(ZZ())

    if sum(A) <= K:
        print(0)
        return

    cost = list()
    for a, f in zip(A, F): cost.append(a*f)

    ok = 10 ** 12
    ng = -1

    while ok - ng > 1:
        mid = (ok+ng)//2
        cc = 0
        for i in range(N): cc += max(0, (cost[i]-mid+F[i]-1)//F[i])
        if cc <= K: ok = mid
        else: ng = mid
    print(ok)

    return

if __name__ == '__main__':
    main()
