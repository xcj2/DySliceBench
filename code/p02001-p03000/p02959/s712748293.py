import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    a_s = LI()
    b_s = LI()
    b_s.append(0)
    ans = 0
    ans += min(a_s[0], b_s[0])
    for i in range(n):
        r = max(b_s[i] - a_s[i], 0)
        # print(a_s, b_s, b_s[i] - a_s[i], a_s[i+1], r)
        if r > a_s[i+1]:
            ans += a_s[i+1]
        else:
            ans += r
        a_s[i+1] = max(a_s[i+1] - r, 0)
        ans += min(a_s[i+1], b_s[i+1])
    print(ans)

if __name__ == '__main__':
    main()