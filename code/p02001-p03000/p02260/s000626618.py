import sys

ERROR_INPUT = 'input is invalid'


def main():
    n = get_length()
    arr = get_array(length=n)

    sourtLi, count = selectionSort(li=arr, length=n)
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


def selectionSort(li, length):
    count = 0

    for i in range(0, length - 1):
        min_index = i
        for j in range(i, length):
            if li[j] < li[min_index]:
                min_index = j

        if i != min_index:
            li[i], li[min_index] = li[min_index], li[i]
            count += 1

    return li, count


main()