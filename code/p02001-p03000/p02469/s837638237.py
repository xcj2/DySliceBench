import math
from typing import List
from functools import reduce

def least_common_multiple(x: int, y: int) -> int:
    return x * y // math.gcd(x, y)


def least_common_multiple_of_numbers(numbers: List[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]

    # while len(numbers) != 1:
    #     new_nums = []
    #     for i in range(len(numbers) // 2):
    #         new_nums.append(least_common_multiple(numbers[2*i], numbers[2*i+1]))
    #     if len(numbers) % 2 != 0:
    #         new_nums.append(numbers[-1])
    #     numbers = new_nums
    # return numbers

    return reduce(least_common_multiple, numbers)


def main():
    m = int(input())
    numbers = list(map(int, input().split()))
    gcm = least_common_multiple_of_numbers(numbers)
    print(gcm)
    return


main()
