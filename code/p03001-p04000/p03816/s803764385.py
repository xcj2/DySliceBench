import collections

def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return not is_even(n)


def solve(n, a):
    counter = collections.Counter(a)

    evens = 0
    odds = 0
    for item in counter.items():
        k, v = item
        if is_odd(v):
            odds += 1
        else:
            evens += 1

    if is_even(evens):
        return odds + evens
    else:
        return odds + (evens - 1)


def get_args():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


if __name__ == '__main__':
    n, a = get_args()
    res = solve(n, a)
    print(res)
