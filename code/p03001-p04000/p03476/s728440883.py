#!/usr/bin/env python3


import itertools


INT_END = 10 ** 5 + 1


def sieve_of_eratosthenes(end, typecode="L"):
    """Enumerates the prime numbers below the given integer.

    :param int end: Prime numbers below this integer will be enumerated.
    :param str typecode: The type of the array to be returned (optional).
    :return: The array of the prime numbers.
    :rtype: :class:`array.array`
    """

    assert end > 1
    is_prime = [True for i in range(end)]
    is_prime[0] = False
    is_prime[1] = False
    # primes = array.array(typecode)
    for i in range(2, end):
        if is_prime[i]:
            # primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    # return primes
    return is_prime


class CumulativeSum(object):
    """Constructs the cumulative sum of the elements in the given sequence.

    :param sequence: The sequence to be processed.
    :type sequence: sequence
    """

    def __init__(self, sequence):
        self.cumulative_sum = [0]
        self.cumulative_sum.extend(itertools.accumulate(sequence))

    def partial_sum(self, first, last):
        """Computes the partial sum of the sequence.

        :param first: The index representing the first element of the
                      subsequence.
        :type first: int
        :param last: The index representing the last element of the
                     subsequence.
        :return: The partial sum.
        """
        return self.cumulative_sum[last + 1] - self.cumulative_sum[first]


def enumerate_like_number(end=INT_END):
    is_prime = sieve_of_eratosthenes(end)
    is_like = [False for _ in range(end)]
    for i in range(1, end, 2):
        if is_prime[i] and is_prime[(i + 1) // 2]:
            is_like[i] = True
    return is_like


def main():
    q = int(input())
    cs = CumulativeSum(enumerate_like_number())
    for _ in range(q):
        l, r = (int(z) for z in input().split())
        print(cs.partial_sum(l, r))


if __name__ == '__main__':
    main()
