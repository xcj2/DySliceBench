from itertools import permutations, combinations

M = 10**9+7


def solve(n, x):
    res = 1
    k = 0
    for i in range(n):
        k += 1
        if x[i] < 2 * k - 1:
            res *= k
            res %= M
            k -= 1
    if k > 0:
        for i in range(1, k+1):
            res *= i
            res %= M
    return res


def solve2(n, x):
    res = 0
    for p in permutations(range(n)):
        done = set()
        ok = True
        for i in range(n):
            can_win = True
            k = 1
            for j in range(p[i]):
                if j in done:
                    continue
                can_win &= x[j] >= k
                k += 2
            ok &= can_win
            done.add(p[i])
        if ok:
            res += 1
    return res


def check():
    for n in range(1, 8):
        for x in combinations(range(1, 2 * n + 1), n):
            expected = solve2(n, list(x))
            output = solve(n, list(x))
            if output != expected:
                print('x: {}'.format(x), end='\t')
                print('output: {}'.format(output), end='\t')
                print('expected: {}'.format(expected), end='\n')
                return x

if __name__ == '__main__':

    # print(check())

    n = int(input())
    x = list(map(int, input().split()))
    print(solve(n, x))
