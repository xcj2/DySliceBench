import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def count_v(last_d, C, S, t, d):
    ret = S[t - 1]
    last_d[t - 1] = d
    for i in range(len(last_d)):
        ret -= C[i] * (d - last_d[i])
    return ret


def main():
    D = int(input())
    C = inpl()
    Ss = [inpl() for _ in range(D)]
    T = [int(input()) for _ in range(D)]
    last_d = [-1] * len(C)

    v = 0
    for d in range(D):
        tmp = count_v(last_d, C, Ss[d], T[d], d)
        v += tmp
        print(v)

    return


if __name__ == '__main__':
    main()
