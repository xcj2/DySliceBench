def calc_n_layers(n):
    memo = {}
    def calc(n):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 1
        ret = 3 + calc_n_layers(n-1)*2
        memo[n] = ret
        return ret
    return calc(n)


def n_patties(n):
    memo = {}
    def calc(n):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 1
        ret = n_patties(n-1)*2 + 1
        memo[n] = ret
        return ret
    return calc(n)


def solve(n, x):
    if x <= 0:
        return 0
    if n <= 0:
        return 1
    l = calc_n_layers(n)
    l2 = (l - 3) // 2
    if x-1 <= l2:
        return solve(n-1, x-1)
    else:
        x = x - 1
        ret = n_patties(n-1)
        x = x - l2
        ret += 1
        x = x - 1
        ret += solve(n-1, x)
        return ret


def main():
    N, X = list(map(int, input().split(' ')))
    print(solve(N, X))

if __name__ == '__main__':
    main()