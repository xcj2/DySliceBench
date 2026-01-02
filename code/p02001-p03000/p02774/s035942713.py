# import numpy as np
stdin = open(0)

N, K = map(int, stdin.readline().split())
# A = np.array(stdin.read().split(), np.int64)
A = list(map(int, stdin.read().split()))

# A = np.sort(A)
# zero = A[A == 0]
# pos = list(A[A > 0])
# neg = list(A[A < 0])

A.sort()
zero = list(filter(lambda x: x == 0, A))
pos = list(filter(lambda x: x > 0, A))
neg = list(filter(lambda x: x < 0, A))

pos_size = len(pos)
neg_size = len(neg)
zero_size = len(zero)

neg_count = pos_size * neg_size
pos_count = pos_size * (pos_size - 1) // 2 + neg_size * (neg_size - 1) // 2
zero_count = N * (N - 1) // 2 - neg_count - pos_count

if K > neg_count and K <= neg_count + zero_count:
    print(0)
    exit(0)

def f(x):
    """x以下の積の組み合わせを数える(k番目が負の場合)"""
    count = 0
    pos_idx = None
    neg_idx = 0
    for idx, p in enumerate(pos):
        if p * neg[neg_idx] <= x:
            pos_idx = idx
            break
    # pos_idxに最大の負の値x正の値 <= xを満たす最小の正値のindexが入っている
    if pos_idx is not None:
        count += pos_size - pos_idx
        # print(pos_idx, count)
        while neg_idx < neg_size - 1:
            neg_idx += 1
            ans = None
            for i in range(pos_idx, pos_size):
                if pos[i] * neg[neg_idx] <= x:
                    ans = i
                    break
            if ans is None:
                break
            count += pos_size - ans
            pos_idx = ans
    return count

def g(x):
    """x以下の積の組み合わせを数える(k番目が正の場合)"""
    count = neg_count + zero_count
    # print('c1', count)
    l_idx = 0
    r_idx = 0
    # 正数 x 正数の場合
    for idx, p in enumerate(reversed(pos)):
        if p * pos[l_idx] <= x:
            r_idx = pos_size - idx - 1
            break
    if r_idx > 0:
        count += (r_idx + 1) - 1  # index = 0の分は引く
        while r_idx - l_idx > 0:
            l_idx += 1
            ans = l_idx
            # print(l_idx, r_idx)
            # for i in reversed(range(l_idx + 1, r_idx + 1)):
            for i in range(r_idx, l_idx, -1):
            # for j in range(l_idx + 1, r_idx + 1):
            #     i = r_idx + l_idx + 1 - j
                if pos[i] * pos[l_idx] <= x:
                    ans = i
                    break
            # print('ans', ans, l_idx)
            if ans > l_idx:
                count += ans - l_idx
                r_idx = ans
            else:
                break
    # print('c2', count)
    # 負数 x 負数の場合
    r_idx = neg_size - 1
    l_idx = neg_size - 1
    for idx, n in enumerate(neg):
        if n * neg[r_idx] <= x:
            l_idx = idx
            break
    # print(l_idx, r_idx)
    if l_idx < r_idx:
        count += neg_size - l_idx - 1 # r_idxの分は引く
        # print('c3', count)
        while r_idx - l_idx > 0:
                r_idx -= 1
                ans = r_idx
                # print(l_idx, r_idx)
                for i in range(l_idx, r_idx):
                    # print(i, pos[i], l_idx, pos[l_idx])
                    if neg[i] * neg[r_idx] <= x:
                        ans = i
                        break
                # print(l_idx, r_idx, ans)
                # print('ans', ans, l_idx)
                if ans < r_idx:
                    count += r_idx - ans
                    l_idx = ans
                else:
                    break
    return count


def h(x):
    return f(x) if K <= neg_count else g(x)


# print(h(-7))

def main():
    l = -1 * 10 ** 18
    r = 10 ** 18
    if K <= neg_count:
        r = 0
        h = f
    else:
        l = 0
        h = g

    while l + 1 < r:
        mid = (l + r) // 2
        count = h(mid)
        # print(mid, count)
        if count >= K:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == "__main__":
    main()
