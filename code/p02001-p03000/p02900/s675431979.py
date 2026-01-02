from math import gcd
import random
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def is_prime3(q, k=50):
    q = abs(q)
    # 計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False

    # n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    # 判定をk回繰り返す
    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        # [0,s-1]の範囲すべてをチェック
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return False
    return True

def factorization(n):
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


A, B = map(int, input().split())
l = make_divisors(gcd(A, B))
_l = factorization(gcd(A, B))
ans = 0
#print(gcd(A, B))
#print(l)
#print(_l)
for num in l:
    if is_prime3(num):
        #print(num)
        ans += 1
print(ans + 1)

