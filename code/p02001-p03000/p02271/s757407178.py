# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_A


def ni():
    return list(map(int, input().split()))


def permutation(A, m):
    from itertools import permutations
    for size in range(len(A)):
        for perm in permutations(A, r=size):
            print(perm)
            if sum(perm) == m:
                return True
    return False


def combination(A, m):
    if sum(A) < m:
        return False

    from itertools import combinations
    for size in range(1, len(A)+1):
        # heavy
        for comb in combinations(A, size):
            if sum(comb) == m:
                return True

    return False


def solve():
    _ = input()
    A = sorted(ni())
    _ = input()
    mi = ni()

    # print(*A)
    # print(*mi)
    # print('yes' for m in mi if permutation(A, m) else 'no')

    for m in mi:
        if combination(A, m):
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    solve()

