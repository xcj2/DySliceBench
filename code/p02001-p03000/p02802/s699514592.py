import sys
from collections import Counter

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    answers = inputs
    n_solve = 0
    n_pena = 0
    solve_progress = set()
    num_answers = Counter({})

    for ans in answers:
        a = ans.split()
        number = int(a[0])
        result = a[1]

        if number in solve_progress:
            continue
        if result == "AC":
            solve_progress.add(number)
            n_solve += 1
        else:
            num_answers[number] += 1

    for s in solve_progress:
        n_pena += num_answers[s]
    return "{} {}".format(n_solve, n_pena)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)
