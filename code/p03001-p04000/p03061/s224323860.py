import sys

def gcd(a, b):
    b, a = sorted([a, b])
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def get_cum_gcd(N, As):
    cum_gcd = [0] * N
    for i, n in enumerate(As):
        if i == 0:
            cum_gcd[i] = n
        else:
            cum_gcd[i] = gcd(cum_gcd[i-1], n)
    return cum_gcd

def get_cav_gcds(N, cum_l, cum_r):
    cav_gcds = [0] * N
    for i in range(N):
        if i == 0:
            cav_gcds[i] = cum_r[i+1]
        elif i == N-1:
            cav_gcds[i] = cum_l[i-1]
        else:
            cav_gcds[i] = gcd(cum_l[i-1], cum_r[i+1])
    return cav_gcds

def main():
    input = sys.stdin.readline
    N = int(input())
    As = list(map(int, input().split()))
    cum_l = get_cum_gcd(N, As)
    cum_r = list(reversed(get_cum_gcd(N, reversed(As))))
    cav_gcds = get_cav_gcds(N, cum_l, cum_r)
    print(max(cav_gcds))

if __name__ == '__main__':
    main()
