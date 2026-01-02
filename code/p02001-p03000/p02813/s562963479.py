import sys


def num_list(nums):
    if len(nums) == 1:
        return [nums]
    result = []
    for num in nums:
        next_nums = nums.copy()
        next_nums.remove(num)
        result += list(map(lambda x: [num] + x, num_list(next_nums)))
    return result


def solve(inp):
    N = int(inp.readline().strip())
    P = list(map(int, inp.readline().strip().split(' ')))
    Q = list(map(int, inp.readline().strip().split(' ')))

    nl = num_list(list(range(1, N + 1)))
    p = nl.index(P)
    q = nl.index(Q)

    return str(abs(p - q))


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
