import itertools, math

N = int(input())
K = int(input())

def cmb(n, r):
    if r < 0 or r > n:
        return 0
    return (math.factorial(n) // math.factorial(r)) // math.factorial(n-r)

def ans_when_K1(N):
    max_digit = len(str(N))
    return 9 * (max_digit-1) + int(str(N)[0])

def ans_when_K2(N):
    max_digit = len(str(N))
    if max_digit < 2:
        return 0

    digit = 2
    ans = 0
    while digit < max_digit:
        ans += 9 * (digit-1) * 9
        digit += 1

    second_non_zero_idx = -1
    for i in range(1, max_digit):
        if str(N)[i] != "0":
            second_non_zero_idx = i
            break

    ans += (int(str(N)[0]) -1) * (digit-1) * 9
    if second_non_zero_idx != -1:
        ans += ans_when_K1(int(str(N)[second_non_zero_idx:]))
    return ans

def ans_when_K3(N):
    max_digit = len(str(N))
    if max_digit < 3:
        return 0

    digit = 3
    ans = 0
    while digit < max_digit:
        ans += 9 * cmb(digit-1, 2) * 9 * 9
        digit += 1

    second_non_zero_idx = -1
    for i in range(1, max_digit):
        if str(N)[i] != "0":
            second_non_zero_idx = i
            break

    ans += (int(str(N)[0]) -1) * cmb(digit-1, 2) * 9 * 9
    if second_non_zero_idx != -1:
        ans += ans_when_K2(int(str(N)[second_non_zero_idx:]))
    return ans

if K == 1:
    print(ans_when_K1(N))
elif K == 2:
    print(ans_when_K2(N))
else:
    print(ans_when_K3(N))