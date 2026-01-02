# -*- coding: utf-8 -*-


def selection_sort(seq, l):
    cnt = 0

    for head_i in range(l):
        flag = False

        min_i = head_i
        for target_i in range(head_i+1, l):
            if seq[target_i] < seq[min_i]:
                min_i = target_i
                flag = True
        if flag:
            seq[head_i], seq[min_i] = seq[min_i], seq[head_i]
            cnt += 1

    print(' '.join([str(n) for n in seq]))
    print(cnt)


def to_int(v):
    return int(v)


def to_seq(v):
    return [int(c) for c in v.split()]


if __name__ == '__main__':
    l = to_int(input())
    seq = to_seq(input())

    selection_sort(seq, l)