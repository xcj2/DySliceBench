def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def two(val):
    ret = 0
    tmp = val
    while True:
        if tmp != 0 and tmp % 2 == 0:
            ret += 1
            tmp = tmp // 2
        else:
            break
    return ret


n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = []

for item in a_list:
    b_list.append(item // 2)

cnt = -1

for item in b_list:
    ret = two(item)
    if cnt == -1:
        cnt = ret
    elif cnt != ret:
        print(0)
        exit()

val = b_list[0]

for item in b_list:
    val = lcm(item, val)

ret = m // val

tmp1 = ret // 2
tmp2 = ret % 2

print(tmp1 + tmp2)
