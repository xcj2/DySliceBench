import sys
mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, pow(b, mod-2,mod))

ivl = [0]
def inverse_max(a): #下2つを使用する際の下準備

    now = 1
    for i in range(a):
        i += 1
        now *= i
        now %= mod
        ivl.append(now)

def nCr(n,r):
    return div(ivl[n] , mul(ivl[n-r] , ivl[r]))


N,M = map(int,input().split())
inverse_max(N + 40)

if N == 1:
    print (1)
    sys.exit()

l = [2]
now = 3

while now ** 2 <= M:
    flag = True
    for i in l:
        if now % i == 0:
            flag = False
            break
    if flag:
        l.append(now)
    now += 2

dic = {}
for i in l:

    while M % i == 0:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

        M //= i

if M != 1:
    dic[M] = 1

ans = 1
#print (dic)

for i in dic:
    ans *= nCr(dic[i] + N - 1,dic[i])
    #print (ans)
    ans %= (10 ** 9 + 7)
print (ans % (10**9+7))