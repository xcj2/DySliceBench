import math


def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]

    p_pos = get_pos(P)
    q_pos = get_pos(Q)
    if p_pos > q_pos:
        print(p_pos - q_pos)
    else:
        print(q_pos - p_pos)


def get_pos(arr):
    len_to_pattern = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    p_pos = 0
    pos = len(arr) - 1
    first = len_to_pattern[pos]
    after = list(arr)
    after.sort()
    i = 0
    for p1 in arr:
        p_pos += first * after.index(p1)
        pos -= 1
        first = len_to_pattern[pos]
        i += 1
        after = arr[i:]
        after.sort()
    return p_pos


def get_max_len(l):
    v = l.sort(reverse=True)[0]
    return len(str(v))


if __name__ == "__main__":
    main()
