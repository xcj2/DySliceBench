import itertools


def solve(x, s_pair, t_pair):
    assert 2 == len(s_pair) == len(t_pair)
    min_dist = 10**11  # large number
    for s, t in itertools.product(s_pair, t_pair):
        min_dist = min([
            min_dist,
            abs(x - s) + abs(s - t),
            abs(x - t) + abs(t - s)
        ])
    return min_dist


def binary_search(x, li):
    lower = 0
    upper = len(li) - 1
    while abs(upper - lower) > 1:
        mid = (lower + upper) // 2
        if li[mid] < x:
            lower = mid
        else:
            upper = mid
    return (li[lower], li[upper])


def main():
    A, B, Q = list(map(int, input().split(' ')))
    s_list = [int(input()) for _ in range(A)]
    s_list.sort()
    t_list = [int(input()) for _ in range(B)]
    t_list.sort()
    x_list = [int(input()) for _ in range(Q)]
    for x in x_list:
        s_pair = binary_search(x, s_list)
        t_pair = binary_search(x, t_list)
        print(solve(x, s_pair, t_pair))


if __name__ == '__main__':
    main()