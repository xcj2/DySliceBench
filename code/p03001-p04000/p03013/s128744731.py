import sys

sys.setrecursionlimit(110000)

d = {}


def calc_step_combination(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    if num in d:
        return d[num]
    res = calc_step_combination(num - 1) + calc_step_combination(num - 2)
    d[num] = res
    return res


def sol(n, a_list):
    step_batch = []
    batch_start = 0
    for a in a_list:
        step_batch.append(a - batch_start)
        batch_start = a + 1
    step_batch.append(n - batch_start + 1)

    result = 1
    for i, steps in enumerate(step_batch):
        result *= calc_step_combination(steps)
    print(result % 1000000007)


def main():
    n, m = map(int, input().split())
    a_list = []
    for i in range(0, m):
        a_list.append(int(input()))
    sol(n, a_list)


main()
