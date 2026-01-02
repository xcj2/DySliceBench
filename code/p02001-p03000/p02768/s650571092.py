import numpy as np
import math as m

def main(**kwargs):
    mod = 10 ** 9 + 7
    r = repeatSquare(2, n, mod) - 1
    r -= factMod(n, n - a + 1, mod) * repeatSquare(factMod(a, 1, mod), mod - 2, mod)
    r -= factMod(n, n - b + 1, mod) * repeatSquare(factMod(b, 1, mod), mod - 2, mod)
    r %= mod
    return r

def repeatSquare(n, p, m):
    if p == 0:
        return 1

    if p % 2 == 0:
        tmp = repeatSquare(n, p/2, m) % m
        return tmp * tmp % m

    return n * repeatSquare(n, p-1, m) % m

def factMod(n, r, m):
    res = n

    while n > r:
        n -= 1
        res *= n
        res %= m

    return res

if __name__ == "__main__":
    
    cin = np.array(input().split(" ")).astype("int")
    n, a, b = cin

    cout = main(n=n, a=a, b=b)
    print(cout)
    