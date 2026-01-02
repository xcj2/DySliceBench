import itertools


def is_compatible_internal(hyp, statement):
    honests = {key for key in statement if statement[key] == 1}
    unkinds = {key for key in statement if statement[key] == 0}

    return len(honests - hyp) == 0 and len(unkinds - hyp) == len(unkinds)


def is_compatible(hyp, statements):
    for i in hyp:
        if not is_compatible_internal(hyp, statements[i]):
            return False
    return True


def main():
    n = int(input())

    all_statements = [{}]
    for _ in range(n):
        ai = int(input())
        statements = {}
        for _ in range(ai):
            x, y = input().split()
            statements[int(x)] = int(y)
        all_statements.append(statements)

    for e in all_cases(n):
        if is_compatible(e, all_statements):
            print(len(e))
            return

    print(0)


def all_cases(n):
    for r in range(n, 0, -1):
        for ensemble in itertools.combinations(range(1, n + 1), r):
            yield set(ensemble)


if __name__ == '__main__':
    main()
