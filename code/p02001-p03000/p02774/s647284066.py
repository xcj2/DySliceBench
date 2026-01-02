MAX = int(10e18)


def count(arr1, arr2, target, remove_dup):
    ret = 0
    j = len(arr2)
    for i, val1 in enumerate(arr1):
        while j > 0 and val1 * arr2[j-1] > target:
            j -= 1
        ret += j
        if remove_dup and j >= (i+1):
            ret -= 1
    if remove_dup:
        ret //= 2
    return ret


def search_negative(pos, neg, K):
    neg.sort()
    pos.sort(reverse=True)
    lo = -MAX
    hi = 0
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = count(pos, neg, mid, False)
        if cnt < K:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_positive(pos, neg, K):
    pos.sort()
    neg.sort(reverse=True)
    lo = 0
    hi = MAX
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = count(pos, pos, mid, True) + count(neg, neg, mid, True)
        if cnt < K:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    negative_nums = []
    positive_nums = []
    zeros = 0
    for a in A:
        if a < 0:
            negative_nums.append(a)
        elif a > 0:
            positive_nums.append(a)
        else:
            zeros += 1
    negative_count = len(negative_nums) * len(positive_nums)
    zero_count = zeros * (N-1) - zeros * (zeros-1) // 2
    ans = 0
    if K <= negative_count:
        ans = search_negative(positive_nums, negative_nums, K)
    elif K <= negative_count + zero_count:
        ans = 0
    else:
        ans = search_positive(positive_nums, negative_nums,
                              K - negative_count - zero_count)
    print(ans)


if __name__ == "__main__":
    main()
