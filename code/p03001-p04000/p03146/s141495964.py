def func_odd(n):
    return int(3 * n + 1)


def func_even(n):
    return int(n / 2)


def is_finished(array):
    before_len = len(array)
    after_len = len(list(set(array)))
    return before_len != after_len


def main(s):
    array = [s]
    index = 0
    while True:
        if array[index] % 2 == 0:
            array.append(func_even(array[index]))
        else:
            array.append(func_odd(array[index]))
        if is_finished(array):
            break
        index += 1
    print(index + 2)


if __name__ == '__main__':
    main(int(input()))
