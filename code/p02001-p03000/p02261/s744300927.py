def buble_sort(seq):
    l = len(seq)
    res = seq[:]
    for i in range(l):
        for j in range(i+1, l)[::-1]:
            if res[j][-1] < res[j-1][-1]:
                res[j], res[j-1] = res[j-1], res[j]
    return res


def selection_sort(seq):
    l = len(seq)
    res = seq[:]
    for i in range(l):
        mi = i
        for j in range(i, l):
            if res[j][-1] < res[mi][-1]:
                mi = j
        if i is not mi:
            res[i], res[mi] = res[mi], res[i]
    return res


def is_stable(seq, sorted_seq):
    card_dic = {s[-1]: [] for s in set(seq)}
    for s in seq:
        key = s[-1]
        card_dic[key].append(s[0])

    for ss in sorted_seq:
        key = ss[-1]
        val = card_dic[key].pop(0)
        if not val == ss[0]:
            return False
    return True


n = int(input())
C = input().split()

b_sorted = buble_sort(C)
print(' '.join(b_sorted))
print('Stable' if is_stable(C, b_sorted) else 'Not stable')

s_sorted = selection_sort(C)
print(' '.join(s_sorted))
print('Stable' if is_stable(C, s_sorted) else 'Not stable')