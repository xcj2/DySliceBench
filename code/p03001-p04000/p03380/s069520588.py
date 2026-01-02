import bisect


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])

def get_comb(num, sort_numbers):
    index = bisect.bisect(sort_numbers, int(num/2))
    left = sort_numbers[index-1]
    right = sort_numbers[index]
    choose_num = left if abs(num/2 - left) < abs(num/2 - right) or right == num else right
    return choose_num

def solve():
    N = get_next_int()
    numbers = get_next_ints()
    max_num, max_choose = 0, -1
    sort_numbers = sorted(numbers)
    for num in sort_numbers[int(len(sort_numbers)/2):][::-1]:
        choose = get_comb(num, sort_numbers)
        if choose > max_choose:
            max_num = num
            max_choose = choose
    print(max_num, max_choose)



solve()