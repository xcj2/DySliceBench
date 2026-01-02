import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    nums = string_to_int(inputs[0])
    count = 0
    for i in range(0, len(nums)-2):
        if nums[i+1] >= nums[i] and nums[i+1] <= nums[i+2]:
            count += 1
        elif nums[i+1] <= nums[i] and nums[i+1] >= nums[i+2]:
            count += 1
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
