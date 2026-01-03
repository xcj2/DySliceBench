import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

def to_minus_one(num):
    return -1 - num

def to_plus_one(num):
    return 1 - num

s_list = np.zeros(n)
s = 0
for i in range(n):
    s += a[i]
    s_list[i] += s


def cal(sum_list, t, ans):
    hoge = 0
    for i in range(n):
        sum_list[i] += hoge
        if (i+t) % 2 == 0:
            if sum_list[i] >= 0:
                hiku = to_minus_one(sum_list[i])
                hoge += hiku
                ans += abs(hiku)
            else:
                continue
        else:
            if sum_list[i] <= 0:
                tasu = to_plus_one(sum_list[i])
                hoge += tasu
                ans += abs(tasu)
    return ans

q = np.copy(s_list)
w = np.copy(s_list)
num1 = cal(q, 0, 0)
num2 = cal(w, 1, 0)

print(int(min(num1, num2)))