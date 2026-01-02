# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0056
"""
from math import sqrt, ceil, pow
import bisect


# https://github.com/mccricardo/sieve_of_atkin/blob/master/sieve_of_atkin.py
class SieveOfAtkin:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.sieve = [False] * (self.limit + 1)

    def flip(self, prime):
        try:
            self.sieve[prime] = True if self.sieve[prime] == False else False
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime] == True: self.sieve[prime] = False
        except KeyError:
            pass

    def isPrime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False

    def getPrimes(self):
        testingLimit = int(ceil(sqrt(self.limit)))

        for i in range(testingLimit):
            for j in range(testingLimit):
                # n = 4*i^2 + j^2
                n = 4 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.flip(n)

                # n = 3*i^2 + j^2
                n = 3 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and n % 12 == 7:
                    self.flip(n)

                # n = 3*i^2 - j^2
                n = 3 * int(pow(i, 2)) - int(pow(j, 2))
                if n <= self.limit and i > j and n % 12 == 11:
                    self.flip(n)

        for i in range(5, testingLimit):
            if self.isPrime(i):
                k = int(pow(i, 2))
                for j in range(k, self.limit, k):
                    self.invalidate(j)

        self.primes = [2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x >= 5]
        return self.primes




def solve1(num, primes):
    # 6.94[s]
    result = 0

    # list_primes = [x for x in primes if x < num]
    i = bisect.bisect_left(primes, num)
    list_primes = primes[:i]


    set_primes = set(list_primes)
    for x in list_primes:
        if x > num/2:
            break
        if (num-x) in set_primes:
            # print('solve1: {} + {} = {}'.format(x, num-x, num))
            result += 1
    return result


def solve2(num, primes):
    result = 0
    sub_primes = set(x for x in primes if x < num)
    while sub_primes:
        x = sub_primes.pop()
        if x*2 == num:
            result += 1
        elif (num-x) in sub_primes:
            result += 1
            sub_primes.remove(num-x)
    return result



def solve3(num, primes):
    # 17.96[s]
    result = 0
    sub_primes = [x for x in primes if x < num]
    primes_len = len(sub_primes)
    # print('solve3: primes_len: {}'.format(primes_len))
    # print(sub_primes)

    n = 0
    while True:
        if sub_primes[n] > num/2:
            break
        i = bisect.bisect_left(sub_primes, num-sub_primes[n])
        if i != primes_len and sub_primes[i] == num-sub_primes[n]:
            # print('solve3: {} + {} = {}'.format(sub_primes[n], num-sub_primes[n], num))
            result += 1
        n += 1
    return result



if __name__ == '__main__':
    A = SieveOfAtkin(50000)
    A.getPrimes()
    while True:
        num = int(input())
        if num == 0:
            break

        # ????????¨???????????¨???
        result = solve1(num, A.primes)
        print(result)