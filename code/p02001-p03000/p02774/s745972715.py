from copy import copy

def solve_negative():
    def count_less_x(x):
        ret = 0
        i = 0
        j = 0
        while i < len(negative_a):
            while j < len(positive_a) and positive_a[j] * negative_a[i] > x:
                j += 1
            ret += len(positive_a) - j
            i += 1

        return ret

    upper = -1
    lower = -1000000001*1000000001
    while upper - lower > 1:
        middle = (upper + lower) // 2
        if count_less_x(middle) >= k:
            upper = middle
        else:
            lower = middle
    return upper


def solve_positive():
    def count_less_x(x):
        ret = 0
        i = 0
        j = len(positive_a) - 1
        while i < len(positive_a):
            while j > i and positive_a[i] * positive_a[j] > x:
                j -= 1
            ret += j - i
            i += 1
            if i >= j:
                break
        i = 0
        j = len(r_negative_a) - 1
        while i < len(r_negative_a):
            while j > i and r_negative_a[i] * r_negative_a[j] > x:
                j -= 1
            ret += j - i
            i += 1
            if i >= j:
                break
        return ret
    lower = 0
    upper = 1000000001*1000000001
    while upper - lower > 1:
        middle = (upper + lower) // 2
        if count_less_x(middle) + num_mul_n + num_mul_z >= k:
            upper = middle
        else:
            lower = middle
    return upper


def solve_zero():
    return 0


def create_sign_split_a(a):
    negative = []
    positive = []
    zero = []
    for x in a:
        if x < 0:
            negative.append(x)
        elif x > 0:
            positive.append(x)
        else:
            zero.append(x)
    return negative, zero, positive


n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

num_n = sum([(a_ < 0) for a_ in a])
num_p = sum([(a_ > 0) for a_ in a])
num_z = sum([(a_ == 0) for a_ in a])
negative_a, zero_a, positive_a = create_sign_split_a(a)
r_negative_a = copy(negative_a)
r_negative_a.reverse()

num_mul_p = num_n * (num_n - 1) // 2 + num_p * (num_p - 1) // 2
num_mul_z = num_n * num_z + num_p * num_z + num_z * (num_z - 1) // 2
num_mul_n = n * (n - 1) // 2 - num_mul_p - num_mul_z


if num_mul_n >= k:
    ans = solve_negative()
elif num_mul_n < k <= num_mul_n + num_mul_z:
    ans = solve_zero()
else:
    ans = solve_positive()
print(ans)
