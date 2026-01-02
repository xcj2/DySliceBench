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
    sento = [[0 for i in range(10)] for i in range(10)]

    vs = [1, 10, 100, 1000, 10000, 100000]
    for i in range(1, n+1):
        m = i % 10
        for v in vs:

            if i // v < 10:

                s = i // v
                break
        # print(i, m, s)
        sento[m][s] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            # print(i, j, sento[i][j], sento[j][i])
            ans += sento[i][j] * sento[j][i]
    print(ans)
    # print(sento)







if __name__ == '__main__':
    main()