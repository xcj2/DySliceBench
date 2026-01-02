import sys

ERROR_INPUT = 'input is invalid'
ERROR_INPUT_NOT_UNIQUE = 'input is not unique'


def main():
    S = get_input1()
    T = get_input2()

    count = 0
    for t in T:
        if linner_search(S, t):
            count += 1

    print(count)


def linner_search(li, key):
    li.append(key)
    i = 0
    while li[i] != key:
        i += 1

    return i != len(li) - 1


def get_input1():
    n = int(input())
    if n > 10000:
        print(ERROR_INPUT)
        sys.exit(1)

    li = []
    for x in input().split(' '):
        if int(x) < 0 or int(x) > 10 ** 9:
            print(ERROR_INPUT)
            sys.exit(1)
        li.append(x)

    return li


def get_input2():
    n = int(input())
    if n > 500:
        print(ERROR_INPUT)
        sys.exit(1)

    li = []
    for x in input().split(' '):
        if int(x) < 0 or int(x) > 10 ** 9:
            print(ERROR_INPUT)
            sys.exit(1)
        elif int(x) in li:
            print(ERROR_INPUT_NOT_UNIQUE)
            sys.exit(1)
        li.append(x)

    return li


main()