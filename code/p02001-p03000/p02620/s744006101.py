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


def count_v_virtual(last_d, C, S, t, d):
    ret = S[t]
    tmp = last_d[t]
    last_d[t] = d
    for i in range(len(last_d)):
        ret -= C[i] * (d - last_d[i])
    last_d[t] = tmp
    return ret


def main():
    D = int(input())
    C = inpl()
    Ss = [inpl() for _ in range(D)]
    T = [int(input()) for _ in range(D)]
    M = int(input())
    DQ = [inpl() for _ in range(M)]
    last_d = [-1] * len(C)
    Contest = 26

    v = 0
    for d in range(D):
        tmp = count_v(last_d, C, Ss[d], T[d], d)
        v += tmp
        # print(v)

    for d, q in DQ:
        diff = 0
        original_t = T[d - 1]
        last_d_q = 0
        last_d_ori = 0
        for i in range(d):
            if T[i] == q:
                last_d_q = i + 1
            if T[i] == original_t and i < d - 1:
                last_d_ori = i + 1
        # print(d, q, original_t, last_d_q, last_d_ori)
        for i in range(d - 1, D):
            if T[i] == q:
                break
            diff += C[q - 1] * (d - last_d_q)
        # print(diff, C[q - 1])
        T[d - 1] = q
        for i in range(d - 1, D):
            if T[i] == original_t:
                break
            diff -= C[original_t - 1] * (d - last_d_ori)
        # print(C[original_t - 1], diff)
        v += diff + Ss[d - 1][q - 1] - Ss[d - 1][original_t - 1]
        print(v)
    return


if __name__ == '__main__':
    main()
