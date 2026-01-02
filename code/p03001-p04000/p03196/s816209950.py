import math
# 素因数分解
def factorize(n):
    if n == 1:
        return [1]
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def f(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 素数判定
def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
           if n%i == 0:
               return False
        return True


n, p = map(int, input().split())

if n == 1 or isPrime(p):
    print(p)
    exit()

# f = factorize(p)
# cnt = [0] * (max(f) + 1)
# # print(f)

# for _f in f:
#     cnt[_f] += 1

# ans = 1
# # print(cnt)

# for i in range(len(cnt)):
#     if cnt[i] >= n:
#         loop = cnt[i]//n
#         for j in range(loop):
#             ans *= i

# print(ans)

f = f(p)
ans = 1

for i in range(len(f)):
    ans *= f[i][0] ** (f[i][1] // n)

print(ans)