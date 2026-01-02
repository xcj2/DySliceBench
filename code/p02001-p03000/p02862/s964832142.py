mod = 1000000007
import sys
sys.setrecursionlimit(1000000)
x, y = map(int, input().split())
a = ((2*x-y)//3)
b = ((2*y-x)//3)
if (x+y) % 3 != 0 or a < 0 or b < 0:
    print(0)
else:
    n = (a + b)%mod
    kaijo = [1, 1]
    for i in range(2, n+1):
        kaijo.append(i*kaijo[i-1]%mod)
    def mul(a, b):
        return ((a % mod) * (b % mod)) % mod
    def power(x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x % mod
        elif y % 2 == 0:
            return power(x, y // 2) ** 2 % mod
        else:
            return power(x, y // 2) ** 2 * x % mod
    def div(a, b):
        return mul(a, power(b, mod - 2))
    n_a = div(kaijo[n], kaijo[a])
    ans = div(n_a, kaijo[n-a])
    print(ans)