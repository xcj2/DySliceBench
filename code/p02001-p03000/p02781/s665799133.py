import sys
input = sys.stdin.buffer.readline

N = int(input())
K = int(input())

LN = len(str(N))

def keta1(n):
    s = str(n)
    return (len(s) - 1) * 9 + int(s[0])
#print(keta1(N))


def keta2(n):
    if n < 10:
        return 0
    cnt2 = [0] * 101
    for i in range(2, 101):
        cnt2[i] = 9 * 9 * (i - 1)
    tmp2 = 0
    for i in range(len(str(n))):
        tmp2 += cnt2[i]
    tmp2 += (int(str(n)[0]) - 1) * keta1((10 ** (len(str(n))  - 1)) - 1) + keta1(int(str(n)[1:]))
    return tmp2

def keta3(n):
    cnt3 = [0] * 101
    for i in range(3, 101):
        cnt3[i] = 9 * 9 * 9 * (i - 1) * (i - 2) // 2
    tmp3 = 0
    for i in range(len(str(n))):
        tmp3 += cnt3[i]
    tmp3 += (int(str(N)[0]) - 1) * keta2((10 ** (len(str(n))  - 1)) - 1) + keta2(int(str(n)[1:]))
    
    return tmp3

if K == 1:
    print(keta1(N))
elif K == 2:
    print(keta2(N))
elif K == 3:
    print(keta3(N))