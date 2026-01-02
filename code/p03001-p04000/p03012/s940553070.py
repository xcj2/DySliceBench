n = int(input())
w_in = input().split()
w = []
for i in range(n):
    w.append(int(w_in[i]))


def list_sum(list):
    result = 0
    for i in range(len(list)):
        result = result+list[i]
    return result


def zettaichi(n):
    if n > 0:
        return n
    else:
        return -1 * n


def sub_devided_at_t(list,t):
    left = list[0:t+1]
    right = list[t+1:]
    sum_left = list_sum(left)
    sum_right = list_sum(right)
    return zettaichi(sum_left - sum_right)


min_result = 100000
for i in range(n):
    if sub_devided_at_t(w,i) < min_result:
        min_result = sub_devided_at_t(w,i)

print(min_result)

