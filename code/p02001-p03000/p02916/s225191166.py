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
    c_s = LI()
    ans = 0
    for i in range(n):
        ans += b_s[a_s[i] - 1]
        if i > 0 and a_s[i-1] + 1 == a_s[i]:
            ans += c_s[a_s[i-1] - 1]
    print(ans)

if __name__ == '__main__':
    main()