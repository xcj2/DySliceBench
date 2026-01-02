# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n, m = MI()
    switch = [0 for _ in range(n)]
    for i in range(m):
        l = LI1()
        k = l[0]
        s = l[1:]
        # print(k, s)
        for ss in s:
            switch[ss] = switch[ss] | (1 << i)

    # print(switch)
    P = 0
    for j, l in enumerate(LI()):
        P = P | (l << j)
    # print(P)

    ans = 0
    for i in range(pow(2, n)):
        x = 0
        # print(bin(i))
        for j in range(n):
            # print('  ', j)
            if 1 & (i >> j):
                # print('    Y', x, switch[j])
                x = x ^ switch[j]
                # print(x)
        if x == P:
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()
