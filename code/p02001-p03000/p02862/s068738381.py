import math
import sys
sys.setrecursionlimit(10000)

X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)
else:
    N_r = int((2*X-Y) / 3)
    N_u = int((2*Y-X) / 3)

    if N_u < 0 or N_r < 0:
        print(0)
    elif N_u == 0 or N_r == 0:
        print(1)
    else:

        mod = 1000000007
        ans = 0

        def power(x, y):
            if   y == 0     :
                return 1
            elif y == 1     :
                return x % mod
            elif y % 2 == 0 :
                return power(x, y//2)**2 % mod
            else            :
                return power(x, y//2)**2 * x % mod

        def mul(a, b):
            return ((a % mod) * (b % mod)) % mod

        def div(a, b):
            return mul(a, power(b, mod-2))


        factorial = [1]
        for n in range(N_r + N_u-1):
            factorial.append(factorial[n]*(n+2)%mod)

        inverse_factorial = [0] * (N_u + N_r)
        inverse_factorial[-1] = power(factorial[-1], mod-2)

        for n in range(N_u+N_r-2, -1, -1):
            inverse_factorial[n] = (inverse_factorial[n+1] * (n+2)) % mod

        def combi(n, m):
            return factorial[n-1] * inverse_factorial[m-1] * inverse_factorial[n-m-1] % mod

        print(int(combi(N_u+N_r, N_u)))
