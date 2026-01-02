

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


def min_cost(li1, li2):
    """calculate minimum cost to transform li1 into li2.

    >>> min_cost([1, 5, 3, 4, 2], [1, 2, 3, 4, 5])
    7
    >>> min_cost([4, 3, 2, 1], [1, 2, 3, 4])
    10
    """
    def find_moves(i, j):
        start = i
        elems = [i]
        mincost = li1[i]
        minidx = 0

        while j != start:
            if mincost > li1[j]:
                mincost = li1[j]
                minidx = len(elems)
            elems.append(j)
            j = li2.index(li1[j])

        elems = elems[minidx+1:] + elems[:minidx+1]
        if 2 * (mincost + li1[mini]) < (len(elems) - 1) * (mincost - li1[mini]):
            elems.append(mini)
            elems.insert(0, mini)

        q = elems.pop()
        p = elems.pop()
        yield (p, q)
        while len(elems) > 0:
            q = p
            p = elems.pop()
            yield (p, q)


    def move(i, j):
        cost = 0
        for p, q in find_moves(i, j):
            li1[p], li1[q] = li1[q], li1[p]
            cost += li1[p] + li1[q]

        return cost

    assert len(li1) == len(li2)
    size = len(li1)
    totalcost = 0

    for i in reversed(range(size)):
        if li1[i] != li2[i]:
            mini = li1.index(li2[0])
            totalcost += move(li1.index(li2[i]), i)

    return totalcost


def run():
    _ = int(input())  # flake8: noqa
    li = [int(i) for i in input().split()]
    sli = li[:]
    (_, sli) = merge_sort(sli)

    print(min_cost(li, sli))


if __name__ == '__main__':
    run()

