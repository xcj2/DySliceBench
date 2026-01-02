import sys
from random import randint
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


def get_diff_score(T, d, q, C, D, Ss):
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
    diff += Ss[d - 1][q - 1] - Ss[d - 1][original_t - 1]
    return diff


def main():
    D = int(input())
    C = inpl()
    Ss = [inpl() for _ in range(D)]
    T = []
    last_d = [-1] * len(C)
    Contest = 26

    v = 0
    for d in range(D):
        tmp_t, tmp_v = -1, -float('inf')
        for i in range(Contest):
            tmp_score = count_v_virtual(last_d, C, Ss[d], i, d)
            if tmp_score > tmp_v:
                tmp_v = tmp_score
                tmp_t = i
        last_d[tmp_t] = d
        v += tmp_v
        T.append(tmp_t + 1)

    Cs = [i + 1 for i, c in enumerate(C)]
    Cs.sort(key=lambda x: C[x - 1])
    c_set = set(Cs[:int(0.1 * len(Cs))])
    c_set_m = Cs[int(0.9 * len(Cs)):]

    for _ in range(30000):
        tmp = [i for i, t in enumerate(T) if t in c_set]
        if len(tmp) < 2:
            break
        i = randint(0, len(tmp) - 1)
        d = randint(0, len(c_set_m) - 1)
        d, q = T[i], c_set_m[d]
        ori_q = T[d - 1]
        diff = get_diff_score(T, d, q, C, D, Ss)
        if diff < -(0.01 * v):
            T[d - 1] = ori_q
        else:
            v += diff

    for _ in range(5000):
        d, q = randint(1, D), randint(1, Contest)
        ori_q = T[d - 1]
        diff = get_diff_score(T, d, q, C, D, Ss)
        if diff < -(0.01 * v):
            T[d - 1] = ori_q
        else:
            v += diff

    for t in T:
        print(t)

    return


if __name__ == '__main__':
    main()
