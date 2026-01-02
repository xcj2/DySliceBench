from bisect import bisect


def check_neg(m, k, pos, neg, len_pos):
    less = 0  # かけたら m 未満になるペア数
    j = 0
    for a in neg:
        d = m // a
        while j < len_pos and pos[j] <= d:
            j += 1
        if len_pos == j:
            break
        less += len_pos - j
    return less < k


def check_pos(m, k, pos, neg, len_pos, len_neg):
    less_eq = 0  # かけたら m 以下になるペア数
    j = 0
    for i in range(len_pos - 1, -1, -1):
        a = pos[i]
        d = m // a
        while j < len_pos and pos[j] <= d:
            j += 1
        if j == len_pos:
            less_eq += len_pos * (i + 1)
            break
        less_eq += j

    j = 0
    for i in range(len_neg - 1, -1, -1):
        a = neg[i]
        d = m // a
        while j < len_neg and neg[j] <= d:
            j += 1
        if j == len_neg:
            less_eq += len_neg * (i + 1)
            break
        less_eq += j

    m_sqrt = int(m ** 0.5)
    less_eq -= bisect(pos, m_sqrt)
    less_eq -= bisect(neg, m_sqrt)

    less_eq //= 2

    return less_eq < k


def solve(n, k, aaa):
    pos = [a for a in aaa if a > 0]
    neg = [a for a in aaa if a < 0]
    len_pos = len(pos)
    len_neg = len(neg)
    neg_mul = len_pos * len_neg
    pos_mul = len_pos * (len_pos - 1) // 2 + len_neg * (len_neg - 1) // 2
    if neg_mul >= k:
        l = -(10 ** 18)
        r = 0
        while l + 1 < r:
            m = (l + r) // 2
            if check_neg(m, k, pos, neg, len_pos):
                l = m
            else:
                r = m
        return l
    elif n * (n - 1) // 2 - pos_mul >= k:
        return 0
    else:
        k -= n * (n - 1) // 2 - pos_mul
        l = 0
        r = 10 ** 18
        neg = [-a for a in neg]
        neg.reverse()
        while l + 1 < r:
            m = (l + r) // 2
            if check_pos(m, k, pos, neg, len_pos, len_neg):
                l = m
            else:
                r = m
        return r


n, k = map(int, input().split())
aaa = list(map(int, input().split()))
aaa.sort()
print(solve(n, k, aaa))


def debug():
    mul = []
    for i in range(n):
        for j in range(i + 1, n):
            mul.append(aaa[i] * aaa[j])
    mul.sort()
    print(mul[k - 1], mul)

# debug()
