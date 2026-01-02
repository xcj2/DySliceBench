def count(nums):
    """count the number of inversions (ai > aj and i < j)
    in a sequence of ints num.

    >>> count([3, 5, 2, 1, 4])
    6
    >>> count([10, 2, 9, 4, 6, 5, 7, 8, 3, 1])
    29
    """
    def _count(i, j):
        if i < j:
            mid = (i + j) // 2
            i1, li1 = _count(i, mid)
            i2, li2 = _count(mid+1, j)

            return _merge(li1, li2, i1 + i2)
        else:
            return (0, nums[i:i+1])

    def _merge(li1, li2, invs):
        i = j = 0
        result = []
        sums = inv = 0
        while i < len(li1) and j < len(li2):
            if li1[i] > li2[j]:
                result.append(li2[j])
                inv += 1
                j += 1
            else:
                result.append(li1[i])
                invs += sums + inv
                sums += inv
                inv = 0
                i += 1

        while i < len(li1):
            result.append(li1[i])
            invs += sums + inv
            sums += inv
            inv = 0
            i += 1
        if j < len(li2):
            result.extend(li2[j:])

        return (invs, result)

    invs, _ = _count(0, len(nums))
    return invs

def run():
    _ = int(input())  # flake8: noqa
    nums = [int(i) for i in input().split()]

    print(count(nums))


if __name__ == '__main__':
    run()

