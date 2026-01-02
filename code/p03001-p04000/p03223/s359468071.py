import sys
fin = sys.stdin.readline

def calc_sum(replaced_list):
    max_sum = 0
    for i in range(len(replaced_list) - 1):
        left, right = replaced_list[i], replaced_list[i + 1]
        max_sum += abs(left - right) 
    return max_sum


def calc_replaced_even(N, A_list, left_mid, right_mid):
    replaced_list = [None] * N
    replaced_list[0] = A_list[left_mid]
    replaced_list[-1] = A_list[right_mid]
    for i in range(1, N//2):
        replaced_list[2 * i - 1] = A_list[-i]
        replaced_list[2 * i] = A_list[i - 1]
    return replaced_list


def calc_replaced_odd(N, A_list, left_mid, right_mid):
    replaced_list = [None] * N
    replaced_list[0] = A_list[left_mid]
    replaced_list[-1] = A_list[right_mid]
    if left_mid == N // 2 - 1:
        replaced_list[1] = A_list[-1]
        for i in range(1, left_mid + 1):
            replaced_list[2 * i] = A_list[i - 1]
            replaced_list[2 * i + 1] = A_list[-(i + 1)]
    else:
        replaced_list[-2] = A_list[0]
        for i in range(1, left_mid):
            replaced_list[2 * i - 1] = A_list[i]
            replaced_list[2 * i] = A_list[-i]
    return replaced_list


def calc_max_sum(replaced_list):
    max_sum = calc_sum(replaced_list)
    replaced_list[1:N-1] = replaced_list[1:N-1][::-1]
    return max(max_sum, calc_sum(replaced_list))


N = int(fin())
A_list = [int(fin()) for _ in range(N)]

A_list.sort()
replaced_list = [None] * N
if N % 2 == 0:
    left_mid = N // 2 - 1
    right_mid = N // 2
    replaced_list = calc_replaced_even(N, A_list, left_mid, right_mid)
    max_sum = calc_max_sum(replaced_list)
    print(max_sum)
else:
    # try 2 types
    max_sum = 0
    for left_mid, right_mid in ((N // 2 - 1, N // 2), (N // 2, N // 2 + 1)):
        replaced_list = calc_replaced_odd(N, A_list, left_mid, right_mid)
        max_sum = max(max_sum, calc_max_sum(replaced_list))
    print(max_sum)
