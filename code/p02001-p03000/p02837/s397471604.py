import itertools


def is_compatible(hyp, testimonies):
    return all((key in hyp) == (val == 1) for key, val in testimonies.items())


def is_compatible_all(hyp, all_testimonies):
    return all(is_compatible(hyp, all_testimonies[i]) for i in hyp)


def main():
    n = int(input())
    all_testimonies = [{}]
    for _ in range(n):
        ai = int(input())
        statements = {}
        for _ in range(ai):
            x, y = input().split()
            statements[int(x)] = int(y)
        all_testimonies.append(statements)

    for e in all_cases(n):
        if is_compatible_all(e, all_testimonies):
            print(len(e))
            return


def all_cases(n):
    for r in range(n, -1, -1):
        for ensemble in itertools.combinations(range(1, n + 1), r):
            yield set(ensemble)


if __name__ == '__main__':
    main()
