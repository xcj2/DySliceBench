SENTINEL = 10**9 + 1


def merge_sort(alist):
    """Sort alist using mergesort.
    Returns a tuple of the number of comparisons and sorted list.

    >>> merge_sort([8, 5, 9, 2, 6, 3, 7, 1, 10, 4])
    (34, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    """
    def _sort(left, right):
        count = 0
        if left + 1 < right:
            mid = (left + right) // 2
            count += _sort(left, mid)
            count += _sort(mid, right)
            count += merge(left, mid, right)

        return count

    def merge(left, mid, right):
        count = 0
        ll = alist[left:mid] + [SENTINEL]
        rl = alist[mid:right] + [SENTINEL]

        i = j = 0
        for k in range(left, right):
            count += 1
            if ll[i] <= rl[j]:
                alist[k] = ll[i]
                i += 1
            else:
                alist[k] = rl[j]
                j += 1

        return count

    comp = _sort(0, len(alist))
    return (comp, alist)


def run():
    _ = int(input())  # flake8: noqa

    li = [int(i) for i in input().split()]

    (c, s) = merge_sort(li)
    print(" ".join([str(i) for i in s]))
    print(c)


if __name__ == '__main__':
    run()

