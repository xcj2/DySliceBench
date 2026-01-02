def calc_50(r, max_num_50):
    if r < 0:
        return 0
    elif r / 50 <= max_num_50:
        return 1
    else:
        return 0


def calc_100(r, max_num_100, max_num_50):
    count = 0
    for num_100 in range(0, max_num_100 + 1):
        count += calc_50(r - 100 * num_100, max_num_50)
    return count


def calc_500(r, max_num_500, max_num_100, max_num_50):
    count = 0
    for num_500 in range(0, max_num_500 + 1):
        count += calc_100(r - 500 * num_500, max_num_100, max_num_50)
    return count


a = int(input())
b = int(input())
c = int(input())
x = int(input())

print(calc_500(x, a, b, c))
