import sys

ERROR_INPUT = 'input is invalid'


def main():
    n = get_length()
    arr = get_array(length=n)
    print(*arr)

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
    for i in range(1, length):
        v = li[i]
        j = i - 1
        while j >= 0 and li[j] > v:
            li[j + 1] = li[j]
            j -= 1

        li[j + 1] = v
        print(*li)


main()