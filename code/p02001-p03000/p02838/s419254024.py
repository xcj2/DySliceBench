import sys

sys.setrecursionlimit(10**7)
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())

def main():
    n = II()
    a_s = LI()
    kaizyo = [1]
    kaizyo_append = kaizyo.append
    keta = [0 for i in range(60)]
    ans = 0
    for i in range(60):
        kaizyo_append(kaizyo[i] * 2 % MOD)
    for i in a_s:
        for j in range(60):
            v, i = i % 2, i // 2
            keta[j] += v
    for i, v in enumerate(keta):
        c = v * (n-v) % MOD
        ans += c * kaizyo[i] % MOD
        ans = ans % MOD

    print(ans)
if __name__ == '__main__':
    main()
