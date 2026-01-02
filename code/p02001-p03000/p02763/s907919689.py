#!/usr/bin/env python3
import sys

sys.setrecursionlimit(300000)



def update(i, val, n, bi_tree, sign=1):
    i += 1
    while i < n:
        bi_tree[i][val] += (1 * sign)
        i += i & -i


def get_sum(i, bi_tree):
    ans = [0] * 26
    while i > 0:
        tmp = bi_tree[i]
        for j in range(26):
            ans[j] += tmp[j]
        i -= i & -i
    return ans


def get_range_sum(left, right, bi_tree):
    r_sum = get_sum(right, bi_tree)
    l_sum = get_sum(left - 1, bi_tree)
    for i in range(26):
        r_sum[i] -= l_sum[i]
    return r_sum


from pprint import pprint

def solve(N, S, Q, queries):
    #arr.insert(0, 0)   # insert dummy node for 1-based indexing
    #bit = [0 for i in range(n+1)]
    bit = [[0] * 26 for i in range(N + 1)]
    s = []
    for i, c in enumerate(S):
        if 'a' <= c <= 'z':
            update(i, ord(c) - ord('a'), N + 1, bit)
        s.append(c)

    for q in queries:
        if q[0] == '1':
            i, c = int(q[1]) - 1, q[2]
            p = s[i]
            update(i, ord(p) - ord('a'), N + 1, bit, -1)
            update(i, ord(c) - ord('a'), N + 1, bit, 1)
            s[i] = c
        if q[0] == '2':
            l, r = int(q[1]), int(q[2])
            counts = get_range_sum(l, r, bit)
            ret = 0
            for x in counts:
                if x > 0:
                    ret += 1
            print(ret)
        #pprint(get_range_sum(1, 5, bit))
        #print(s)
        #print()

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    S = str(next(tokens))
    Q = int(next(tokens))
    q = []
    for i in range(Q):
        q.append(list(map(str, input().split())))
    solve(N, S, Q, q)

if __name__ == '__main__':
    main()
