# coding: utf-8

# https://atcoder.jp/contests/abc084/tasks/abc084_d
# 18:49-19:10 中断
# 0:21-1:10 done


def prime_set(limit=10**5):
    ret = [2]
    for x in range(3, limit+1, 2):
        is_prime = True
        sqrtx = int(pow(x, 0.5))

        for p in ret:
            if p > sqrtx:
                break

            if x % p == 0:
                is_prime = False
                break

        if is_prime:
            ret.append(x)

    return ret


def bin_search(xs, start, end, x):
    idx = start + (end-start) // 2
    if x < xs[idx]:
        return bin_search(xs, start, idx, x)
    elif x > xs[idx]:
        return bin_search(xs, idx+1, end, x)
    else:
        return idx


def geq_search(xs, start, end, x):
    if end - start < 2:
        if x <= xs[start]:
            return start
        else:
            return start+1

    idx = start + (end-start) // 2

    if x <= xs[start]:
        return start
    elif xs[idx-1] < x <= xs[idx]:
        return idx

    if x < xs[idx]:
        return geq_search(xs, start, idx+1, x)
    elif x > xs[idx]:
        return geq_search(xs, idx, end, x)
    else:
        return idx


def leq_search(xs, start, end, x):
    if end - start < 2:
        if x >= xs[start+1]:
            return start+1
        else:
            return start

    idx = start + (end-start) // 2

    if x >= xs[end-1]:
        return end-1
    elif xs[idx-1] <= x < xs[idx]:
        return idx-1

    if x < xs[idx]:
        return leq_search(xs, start, idx+1, x)
    elif x > xs[idx]:
        return leq_search(xs, idx, end, x)
    else:
        return idx


def main():
    # primes = prime_set(100)
    # print(primes)
    # print(len(primes))
    # print(leq_search(primes, 0, len(primes), 2))
    # print(leq_search(primes, 0, len(primes), 3))
    # print(leq_search(primes, 0, len(primes), 96))
    # print(leq_search(primes, 0, len(primes), 97))
    # exit()

    primes = prime_set()
    primes_set = set(primes)
    len_primes = len(primes)

    Q = int(input())
    l, r = [None] * Q, [None] * Q
    for i in range(Q):
        l[i], r[i] = map(int, input().split())

    # output = 0
    likes = []
    for x in primes[1:]:
        if (x+1) // 2 in primes_set:
            likes.append(x)
    n_likes = len(likes)
    # print(likes)

    for i in range(Q):
        left_idx = geq_search(likes, 0, n_likes, l[i])
        right_idx = leq_search(likes, 0, n_likes, r[i])

        output = right_idx - left_idx + 1 if right_idx >= left_idx else 0
        print(output)

    # for i in range(Q):
    #     output = 0

    #     left, right = l[i], r[i]
    #     while True:
    #         if left in primes_set:
    #             break

    #         left += 2
    #     while True:
    #         if right in primes_set:
    #             break

    #         right -= 2

    #     left_idx = bin_search(primes, 0, len_primes, left)
    #     right_idx = bin_search(primes, 0, len_primes, right)

    #     for x in primes[left_idx:right_idx+1]:
    #         if (x + 1) // 2 in primes_set:
    #             output += 1

    #     print(output)
    # # return output


main()
# print(main())
