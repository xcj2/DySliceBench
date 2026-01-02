import numpy as np


def enum_753_number():
    enum_array = [3, 5, 7]
    enum_array = enum_753_number_(enum_array, 1)
    return enum_array


def enum_753_number_(enum_array, now_digit):
    now_digit += 1;
    if (now_digit > 9):
        return enum_array
    else:
        enum_3_array = [10*num + 3 for num in enum_array]
        enum_5_array = [10*num + 5 for num in enum_array]
        enum_7_array = [10*num + 7 for num in enum_array]
        enum_array.extend(enum_753_number_(enum_3_array, now_digit))
        enum_array.extend(enum_753_number_(enum_5_array, now_digit))
        enum_array.extend(enum_753_number_(enum_7_array, now_digit))
        return enum_array


def check_753_number(number):
    flag_3 = False
    flag_5 = False
    flag_7 = False
    if (number < 100):
        return False
    while (number > 1):
        if (number % 10 == 3): flag_3 = True
        if (number % 10 == 5): flag_5 = True
        if (number % 10 == 7): flag_7 = True
        number = int(number / 10)
    if (flag_3 == True and flag_5 == True and flag_7 == True):
        return True
    else:
        return False


def main():
    string = input()
    N = int(string)
    count = 0
    enum_array = enum_753_number()
    for elem in enum_array:
        if (elem <= N and check_753_number(elem)): count+=1
    print(count)


if __name__ == '__main__':
    main()
