import sys

ERROR_INPUT = 'input is invalid'


def main():
    n = get_length()
    arr = get_array(length=n)

    insetionSort(li=arr, length=n)
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
    if n < 0 or n > 1000:
        print(ERROR_INPUT)
        sys.exit(1)
    else:
        return n


def insetionSort(li, length):
    for n in range(0, length):
        print(*(sorted(li[0:n + 1]) + li[n + 1:length]))


main()