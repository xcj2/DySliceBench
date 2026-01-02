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
    b_s = LI()
    a_s = [0 for i in range(n)]
    for i in range(n-1):
        if i == 0:
            a_s[i] = b_s[i]
            a_s[i+1] = b_s[i]
        else:
            if b_s[i] < b_s[i-1]:
                a_s[i] = b_s[i]
            a_s[i + 1] = b_s[i]
    print(int(sum(a_s)))

if __name__ == '__main__':
    main()