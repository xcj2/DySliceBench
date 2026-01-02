# encoding: utf-8
import sys
# input = sys.stdin.readline
P = 10 ** 9 + 7

N, K = map(int, input().split())

# molec = 1
# for i in range(K - 1):
#     molec = (molec * (i + 1)) % P

power = 10 ** 9 + 5
digits = []
for i in range(64):
    digits.append(power % 2)
    power >>= 1

def modinv(b):
    binv = 1
    val = b % P
    for i, digit in enumerate(digits):
        if digit == 1:
            binv = (binv * val) % P
        val = (val * val) % P
    # print("##", b, binv)
    return binv

molec = 1
tab_nck = [1]
for i in range(1, K - 1):
    molec = (molec * (K - i)) % P
    molec = (molec * modinv(i)) % P
    tab_nck.append(molec)
tab_nck.append(1)

molec = 1
tab_nck2 = [1]
for i in range(1, N - K + 1):
    molec = (molec * (N - K + 2 - i)) % P
    molec = (molec * modinv(i)) % P
    tab_nck2.append(molec)
tab_nck2.append(1)

# print("#", tab_nck)
# print("#", tab_nck2)

def nck(a, b):
    # a = K - 1
    if b < 0: return 0
    elif b > K - 1: return 0
    else: return tab_nck[b]

def nck2(a, b):
    # a = N - K + 1
    if b < 0: return 0
    elif b > N - K + 1: return 0
    else: return tab_nck2[b]

for i in range(1, K + 1):
    ans = 1
    #
    ans = (ans * nck(K - 1, i - 1)) % P
    ans = (ans * nck2(N - K + i - 1, i)) % P
    #
    print(ans)
