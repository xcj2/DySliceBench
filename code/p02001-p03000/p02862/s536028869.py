import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

MOD = 10**9+7

def calc(x, y):
    return int((x + y) / 3), int((2*x - y) / 3)

def mod_cmb(n, r, mod):
    if r == 0:
        return 1
    x = 1
    y = n
    for i in range(2,r+1):
        x *= i
        x %= mod
        y *= n-i+1
        y %= mod
    return y * pow(x, mod-2, mod) % mod


def main():
    x, y = input_nums()
    if (x+y) % 3 != 0:
        print(0)
        exit(0)
    n, m = calc(x, y)
    if n < 0 or m < 0:
        print(0)
        exit(0)
    ans = mod_cmb(n, m, MOD)
    print(ans % MOD)

if __name__ == '__main__':
    main()
