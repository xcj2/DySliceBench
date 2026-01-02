N = int(input())

def max_positive_num(L):
    val = 0
    for i in range(L):
        if i % 2 == 0:
            val = val + 2 ** i
    return val


def min_negative_num(L):
    val = 0
    for i in range(L):
        if i % 2 == 1:
            val = val - 2 ** i
    return val


# 与えた数字に対して最大のビット数を返す
def maxbit(num):
    count = 0
    while not (min_negative_num(count) <= num <= max_positive_num(count)):
        count = count + 1
    return count

bitlist = [0]*maxbit(N)

if N == 0:
    print("0")
else:
    rest = N
    for i in range(maxbit(N), 0, -1):
        if i % 2 == 0:
            if (min_negative_num(i) <= rest < min_negative_num(i-1)):
                bitlist[i-1] = 1
                rest = rest - pow(-2,(i-1))
        else:
            if (max_positive_num(i-1) < rest <= max_positive_num(i)):
                bitlist[i-1] = 1
                rest = rest - pow(-2,(i-1))
    ans = ''.join(map(str, bitlist))
    print(ans[::-1])