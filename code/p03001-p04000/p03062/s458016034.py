#!/usr/bin/env python3

def abs_list_sum(numbers):
    result = 0
    for v in numbers:
        result += abs(v)
    return result


def abs_min(numbers):
    result = abs(numbers[0])
    for v in numbers:
        if result > abs(v):
            result = abs(v)
    return result

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # count negative
    negative_count = 0
    for v in a:
        if v < 0:
            negative_count += 1
    if negative_count % 2 == 0:
        print(abs_list_sum(a))
    else:
        minimum = abs_min(a)
        print(abs_list_sum(a) - 2 * minimum)


if __name__ == '__main__':
    main()
