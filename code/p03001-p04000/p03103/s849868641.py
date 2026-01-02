from collections import defaultdict as dd

# お約束
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(*args):
    return tuple(p(v) for p, v in zip(args, input().split()))

# エントリーポイント
def main():
    N, M = parse(int, int)

    AB = dd(int)
    for _ in range(N):
        a, b = parse(int, int)
        AB[a] += b
    shops = sorted(AB.keys())

    m, cost = M, 0
    for price in shops:
        count = AB[price]
        if m <= count:
            cost += price * m
            break
        else:
            cost += price * count
            m -= count
    print(cost)

main()
