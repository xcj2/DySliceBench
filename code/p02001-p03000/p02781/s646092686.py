N = int(input())
K = int(input())

def keta1(n):
    s = str(n)
    return (len(s) - 1) * 9 + int(s[0])

def keta2(n):
    if n < 10:
      return 0
    s = str(n)
    cnt = [0] * 101
    for i in range(2, 101):
        cnt[i] = 9 * 9 * (i - 1)
    res = 0
    for i in range(len(s)):
        res += cnt[i]
    res += (int(s[0]) - 1) * keta1(10 ** (len(s) - 1) - 1) + keta1(int(s[1:]))
    return res

def keta3(n):
    s = str(n)
    cnt = [0] * 101
    for i in range(3, 101):
        cnt[i] = 9 * 9 * 9 * (i - 1) * (i - 2) // 2
    res = 0
    for i in range(len(s)):
        res += cnt[i]
    res += (int(s[0]) - 1) * keta2(10 ** (len(s) - 1) - 1) + keta2(int(s[1:]))
    return res

if K == 1:
    print(keta1(N))
elif K == 2:
    print(keta2(N))
elif K == 3:
    print(keta3(N))