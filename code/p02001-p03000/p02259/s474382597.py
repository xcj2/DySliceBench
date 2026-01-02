import sys

ERROR_INPUT = 'input is invalid'


def main():
    n = get_length()
    arr = get_array(length=n)

    sourtLi, count = bubbleSort(li=arr, length=n)
    print(*sourtLi)
    print(count)
    return 0


def get_length():
    n = int(input())
    if n < 0 or n > 100:
        print(ERROR_INPUT)
        sys.exit(1)
    else:
        return n


def get_array(length):
    nums = input().split(' ')
    return [str2int(string=n) for n in nums]


def str2int(string):
    n = int(string)
    if n < 0 or n > 100:
        print(ERROR_INPUT)
        sys.exit(1)
    else:
        return n


def bubbleSort(li, length):
    count = 0
    for n in range(length):
        for n in range(1, length - n):
            if li[n] < li[n - 1]:
                li[n], li[n - 1] = li[n - 1], li[n]
                count += 1

    return li, count


main()