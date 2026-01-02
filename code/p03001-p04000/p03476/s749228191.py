import math


class LR:
    def __init__(self, l, r):
        self.left = l
        self.right = r


def is_prime(num):
    if (num < 2):
        return False
    elif(num == 2):
        return True
    elif (num % 2 == 0):
        return False
    sqrt_num = int(math.sqrt(num))
    for i in range(3, sqrt_num+1):
        if i % 2 == 0:
            continue
        if (num % i == 0):
            return False
    return True


def generate_prime_dict():
    prime_dict = {}
    for num in range(1, 100001):
        if is_prime(num):
            prime_dict[num] = 1
    return prime_dict


prime_dict = generate_prime_dict()

like_2017_dict = {}

cnt = 0
for n in range(100001):
    if n in prime_dict and ((n+1)/2) in prime_dict:
        cnt += 1
    like_2017_dict[n] = cnt


Q = int(input())
lrs = []
for _ in range(Q):
    l, r = map(int, input().split())
    lrs.append(LR(l, r))

for lr in lrs:
    print(like_2017_dict[lr.right] - like_2017_dict[lr.left-1])
