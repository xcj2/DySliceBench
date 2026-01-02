def count_descending(nums, start):
    if start >= len(nums):
        return 0

    count = 1
    previous = nums[start]
    for i in range(start + 1, len(nums)):
        if previous < nums[i]:
            return count
        else:
            count += 1
            previous = nums[i]

    return count


def max_move(nums):
    start = 0
    current_max = 0
    while start < len(nums):
        n = count_descending(nums, start)
        current_max = max(current_max, n)
        start += n

    return current_max


def main():
    n = int(input())
    h = [int(x) for x in input().split()]

    print(max_move(h) - 1)


if __name__ == "__main__":
    main()
