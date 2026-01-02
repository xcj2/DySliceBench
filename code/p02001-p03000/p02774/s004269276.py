# https://note.com/tanon_cp/n/ne423915acdaa
from bisect import bisect

INF = 10 ** 18

def check_neg(m, k, pos, neg):
    len_pos = len(pos)
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

def check_pos(m, k, pos, neg):
    less_eq = 0  # かけたら m 以下になるペア数
    j = 0
    len_pos = len(pos)
    len_neg = len(neg)
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


def solve(n, k, A):
    pos = []
    neg = []
    zeros = []
    for a in A:
        if a == 0:
            zeros.append(a)
        elif a > 0:
            pos.append(a)
        else:
            neg.append(a)

    pos = [a for a in A if a > 0]
    neg = [a for a in A if a < 0]
    num_neg = len(neg) * len(pos)
    num_zero = (len(neg) + len(pos)) * len(zeros) + len(zeros) * (len(zeros) - 1) // 2
    if k <= num_neg:
        l = -INF
        r = 0
        while l + 1 < r:
            m = (l + r) // 2
            if check_neg(m, k, pos, neg):
                l = m
            else:
                r = m
        return l
    elif num_neg < k <= num_neg + num_zero:
        return 0
    else:
        k -= (num_neg + num_zero)
        l = 0
        r = INF
        neg = [-a for a in neg]
        neg.reverse()
        while l + 1 < r:
            m = (l + r) // 2
            if check_pos(m, k, pos, neg):
                l = m
            else:
                r = m
        return r


n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(solve(n, k, A))
