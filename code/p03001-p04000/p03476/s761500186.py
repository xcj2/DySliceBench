import math

def is_prime_sqrt(q): #合成数xはp<=sqrt(x)を満たす素因子pを持つ
    if q == 1: #1は素数ではない
        return False
    if q == 2: #2は素数
        return True
    elif q % 2 == 0: #2以外の偶数は合成数
        return False
    for divisor in range(3, math.floor(math.sqrt(q))+1, 2): #繰り返しの上限は平方根
        if q % divisor == 0: #平方根までに約数があれば合成数
            return False
    return True

def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def sieve(n): #nまでの素数をエラトステネスの篩で列挙＝戻り値は各要素が素数のリスト
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return [i for i in range(0,n) if s[i] and i > 1]

def sieveyn(n): #nまでの素数をエラトステネスの篩で列挙＝戻り値は各要素が素数のリスト
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return s


Q = int(input())
A = [0] * 100001 #A[0]からA[100000]までのリスト
A[3] = 1
S = sieveyn(100000)

for i in range(5,100001,4):
    if S[i] and S[int((i+1)/2)]:
        A[i] = 1
for i in range(4,100001):
    A[i] += A[i-1]

#print(A[:100])

for i in range(Q):
    l, r = map(int, input().split())
    print(A[r]-A[l-1])
