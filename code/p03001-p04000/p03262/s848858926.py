import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def kouyakusuu(kyori, num):
    ans = kyori[0]
    pre = kyori[0]
    for i in range(num - 1):
        now_point = kyori[i + 1]
        while now_point:
            pre, now_point = now_point, pre % now_point
        if pre < ans:
            ans = pre
        pre = kyori[i + 1]
    return ans


def main():
    num, start = map(int, input().split())
    data = list(map(int, input().split()))
    kyori = [0 for i in range(num)]

    for i in range(num):
        kyori[i] = abs(data[i] - start)

    ans = kouyakusuu(kyori, num)

    print(ans)





if __name__ == '__main__':
    main()