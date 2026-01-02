from math import ceil


def log(s):
    # print("| " + str(s), file=sys.stderr)
    pass


def output(x):
    print(x, flush=True)


def input_ints():
    return map(int, input().split())


cache = dict()


def solve(goal, count, meta):
    if (goal <= 0):
        return count

    s = frozenset([m[1] for m in meta])
    if s in cache:
        return cache[s]

    min_count = 999999999

    for m in meta:
        meta2 = list(meta)
        meta2.remove(m)
        c = solve(goal - m[3], count + m[0], meta2)
        if c < min_count:
            min_count = c

    for m in reversed(meta):
        if goal - m[0] * m[1] > 0:
            continue
        c = count + ceil(goal / m[1])
        if c < min_count:
            min_count = c
        break

    cache[s] = min_count

    return min_count


def main():
    d, goal = tuple(input_ints())

    meta = list()
    for i in range(d):
        problems, bonus = tuple(input_ints())
        score = (i + 1) * 100
        meta.append((problems, score, bonus, score * problems + bonus))

    count = solve(goal, 0, meta)
    print(count)


main()
