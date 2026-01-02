from sys import stdin

def partition(cards, start, end):
    p = cards[end]
    p_idx = start
    for i in range(start, end):
        c = cards[i]
        if c[1] <= p[1]:
            cards[i], cards[p_idx] = cards[p_idx], cards[i]
            p_idx = p_idx + 1
    cards[p_idx], cards[end] = cards[end], cards[p_idx]
    return p_idx


# in-place quicksort
def quicksort(cards, start, end):
    if start < end:
        p_idx = partition(cards, start, end)
        quicksort(cards, start, p_idx - 1)
        quicksort(cards, p_idx + 1, end)


def merge(nums, left, mid, right):
    l = nums[left:mid] + [('_', 9999999999)]
    r = nums[mid:right] + [('_', 9999999999 )]
    l_cur = 0
    r_cur = 0
    for i in range(right - left):
        if l[l_cur][1] > r[r_cur][1]:
            nums[left + i] = r[r_cur]
            r_cur = r_cur + 1
        else:
            nums[left + i] = l[l_cur]
            l_cur = l_cur + 1


def mergesort(nums, left, right):
    if right - left <= 1:
        return nums
    else:
        mid = (left + right) // 2
        mergesort(nums, left, mid)
        mergesort(nums, mid, right)
        merge(nums, left, mid, right)


def is_stable_result(orig, result):
    stable_result = orig[:]
    mergesort(stable_result, 0, len(stable_result))
    is_stable = True
    for c1, c2 in zip(stable_result, result):
        if c1 != c2:
            is_stable = False
    return is_stable


def parseLine(l):
    kind, num = l.strip().split(' ')
    return (kind, int(num))


def main():
    _, *lines = stdin.readlines()
    nums = [parseLine(l) for l in lines]

    # sort
    result = nums[:]
    quicksort(result, 0, len(result) - 1)

    # check is stable
    is_stable = is_stable_result(nums, result)
    print('Stable' if is_stable else 'Not stable')
    print('\n'.join([kind + ' ' + str(num) for (kind, num) in result]))

if __name__ == '__main__':
    main()
