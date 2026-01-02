import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def extgcd(a, b):
    if b == 0:
        return [1, 0, a]
    x, y, g = extgcd(b, a % b)
    return [y, x - a//b * y, g]


def mod_inverse(a, m):
    x, _, _ = extgcd(a, m)
    return (m + x % m) % m


def mod_comb(n, k, mod):
    mul, div = 1, 1
    for i in range(k):
        mul *= (n-i)
        div *= (i+1)
        mul %= mod
        div %= mod
    return mul * mod_inverse(div, mod) % mod


def main():
    
    x, y = map(int, readline().split())
    if (x+y)%3!=0:
        print(0)
        return
    n = (x+y)//3
    a, b = (2*y-x)//3, (2*x-y)//3
    if a<0 or b<0:
        print(0)
        return
    print(mod_comb(n, min(a, b), (10**9+7)))

if __name__ == "__main__":
    main()
