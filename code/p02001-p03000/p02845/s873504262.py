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
    d = [0, 0, 0]
    ans = 1
    for i in a_s:
        flag = True
        tmp = 0
        for index, j in enumerate(d):
            # print(i, j)
            if j == i:
                tmp += 1
                if flag:
                    d[index] += 1
                    flag = False
        ans = ans * tmp % MOD
        # print(d, tmp, i, ans)
    print(ans)





if __name__ == '__main__':
    main()