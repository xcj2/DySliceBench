
import operator


def permutations(li):
    """Returns a list of previous, current, and
    next permutations of li.

    >>> permutations([1, 2])
    [[1, 2], [2, 1]]
    >>> permutations([1, 3, 2])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3]]
    """
    def perm(op):
        def func(xs):
            i = len(xs) - 1
            while i > 0 and op(xs[i-1], xs[i]):
                i -= 1
            if i > 0:
                i -= 1
                j = i + 1
                while j < len(xs) and op(xs[j], xs[i]):
                    j += 1
                xs[i], xs[j-1] = xs[j-1], xs[i]
                return xs[:i+1] + list(reversed(xs[i+1:]))
            else:
                return None
        return func

    prev_perm = perm(operator.lt)
    next_perm = perm(operator.gt)

    ps = []

    pp = prev_perm(li[:])
    if pp is not None:
        ps.append(pp)

    ps.append(li[:])

    np = next_perm(li[:])
    if np is not None:
        ps.append(np)
    return ps


def run():
    n = int(input())
    li = [int(x) for x in input().split()]
    assert(n == len(li))

    for ps in permutations(li):
        print(" ".join([str(x) for x in ps]))


if __name__ == '__main__':
    run()

